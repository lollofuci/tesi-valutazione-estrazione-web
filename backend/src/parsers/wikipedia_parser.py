import re
from urllib.parse import urlparse, unquote

from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

from parsers.base_parser import BaseParser


class WikipediaParser(BaseParser):
    """Parser dedicato alle pagine Wikipedia."""

    def __init__(self) -> None:
        self.browser_config = BrowserConfig(headless=True)

    async def parse(self, url: str) -> dict:
        """Esegue il parsing di una pagina Wikipedia usando l'HTML."""
        domain = urlparse(url).netloc
        fallback_title = self._extract_title_from_url(url)

        run_config = CrawlerRunConfig(
            word_count_threshold=1,
            remove_overlay_elements=False,
            exclude_external_links=False,
            exclude_social_media_links=False,
            process_iframes=False,
        )

        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            result = await crawler.arun(url=url, config=run_config)

        if not result.success:
            error_message = getattr(result, "error_message", "Errore sconosciuto")
            raise ValueError(f"Errore nel parsing di {url}: {error_message}")

        html_text = result.html or ""
        if not html_text.strip():
            raise ValueError("HTML vuoto: impossibile parsare la pagina.")

        parsed_text, extracted_title = self._parse_wikipedia_html(
            raw_html=html_text,
            fallback_title=fallback_title,
        )

        return {
            "url": url,
            "domain": domain,
            "title": extracted_title,
            "html_text": html_text,
            "parsed_text": parsed_text,
        }

    def _extract_title_from_url(self, url: str) -> str:
        """
        Estrae un titolo affidabile dalla parte finale dell'URL.

        Esempio:
        https://it.wikipedia.org/wiki/Avellino -> Avellino
        """
        path = urlparse(url).path
        slug = path.split("/wiki/")[-1]
        slug = unquote(slug)
        slug = slug.replace("_", " ")
        return slug.strip()

    def _parse_wikipedia_html(self, raw_html: str, fallback_title: str) -> tuple[str, str]:
        """
        Estrae il contenuto informativo principale da una pagina Wikipedia.
        Usa più strategie di fallback.
        """
        soup = BeautifulSoup(raw_html, "html.parser")
        page_title = self._extract_title_from_html(soup, fallback_title)

        root_candidates = [
            soup.select_one("div.mw-parser-output"),
            soup.select_one(".mw-body-content"),
            soup.select_one("#mw-content-text"),
            soup.select_one("#bodyContent"),
            soup.body,
        ]

        blocks: list[str] = []

        for root in root_candidates:
            if root is None:
                continue

            candidate_blocks = self._extract_blocks_from_root(root)
            if candidate_blocks:
                blocks = candidate_blocks
                break

        if not blocks:
            blocks = self._extract_blocks_from_root(soup)

        if not blocks:
            blocks = self._extract_visible_text_lines(soup)

        cleaned_blocks = self._post_process_blocks(blocks)

        if not cleaned_blocks:
            return f"# {page_title}", page_title

        body = "\n\n".join(cleaned_blocks).strip()
        body = self._cut_tail_sections(body)

        if not body:
            return f"# {page_title}", page_title

        return f"# {page_title}\n\n{body}".strip(), page_title

    def _extract_title_from_html(self, soup: BeautifulSoup, fallback_title: str) -> str:
        """
        Estrae il titolo dall'HTML, con fallback all'URL.
        """
        title_candidates = [
            soup.select_one("span.mw-page-title-main"),
            soup.select_one("h1.firstHeading"),
            soup.select_one("title"),
        ]

        for candidate in title_candidates:
            if candidate is None:
                continue

            text = candidate.get_text(" ", strip=True)
            text = re.sub(r"\s+", " ", text).strip()

            if not text:
                continue

            text = text.replace(" - Wikipedia", "")
            text = text.replace(" - Wikipedia, l'enciclopedia libera", "")
            return text

        return fallback_title

    def _extract_blocks_from_root(self, root) -> list[str]:
        """
        Estrae blocchi di testo informativo da un contenitore HTML.
        Supporta paragrafi, heading, liste, definizioni e tabelle.
        """
        root_copy = BeautifulSoup(str(root), "html.parser")

        selectors_to_remove = [
            "style",
            "script",
            "noscript",
            "table.infobox",
            "table.sinottico",
            "table.vertical-navbox",
            "div.navbox",
            "div.metadata",
            "span.mw-editsection",
            "sup.reference",
            "div.reflist",
            "ol.references",
            "div.refbegin",
            "div.thumb",
            "figure",
            "table.wikitable.navbox",
            "div.sidebar",
            "div.toc",
            "#catlinks",
            ".authority-control",
            ".mw-authority-control",
            ".ambox",
            ".tmbox",
            ".ombox",
            ".navbox",
            ".noprint",
            "nav",
            "header",
            "footer",
            "form",
        ]

        for selector in selectors_to_remove:
            for tag in root_copy.select(selector):
                tag.decompose()

        blocks: list[str] = []
        seen_blocks: set[str] = set()

        target_elements = root_copy.find_all(
            ["h2", "h3", "h4", "p", "ul", "ol", "dl", "table"],
            recursive=True,
        )

        for element in target_elements:
            text = self._element_to_text(element)
            if not text:
                continue

            if self._is_noise_line(text):
                continue

            if element.name in {"h2", "h3", "h4"}:
                heading = self._clean_heading(text)
                if not heading:
                    continue

                level = {"h2": "##", "h3": "###", "h4": "####"}[element.name]
                block = f"{level} {heading}"
            else:
                block = text.strip()

            if not block or block in seen_blocks:
                continue

            seen_blocks.add(block)
            blocks.append(block)

        return blocks

    def _extract_visible_text_lines(self, soup: BeautifulSoup) -> list[str]:
        """
        Ultimo fallback: prende il testo visibile globale della pagina.
        """
        body = soup.body or soup
        text = body.get_text("\n", strip=True)
        lines = [self._normalize_text(line) for line in text.splitlines()]

        cleaned_lines: list[str] = []
        seen_lines: set[str] = set()

        for line in lines:
            if not line:
                continue
            if len(line) < 25:
                continue
            if self._is_noise_line(line):
                continue
            if line in seen_lines:
                continue
            seen_lines.add(line)
            cleaned_lines.append(line)

        return cleaned_lines

    def _element_to_text(self, element) -> str:
        """
        Converte un elemento HTML in testo leggibile.
        """
        if element.name == "p":
            text = element.get_text(" ", strip=True)
            return self._normalize_text(text)

        if element.name in {"ul", "ol"}:
            return self._list_to_text(element)

        if element.name == "dl":
            parts = []
            for child in element.find_all(["dt", "dd"], recursive=False):
                child_text = self._normalize_text(child.get_text(" ", strip=True))
                if child_text and not self._is_noise_line(child_text):
                    parts.append(child_text)
            return "\n".join(parts).strip()

        if element.name in {"h2", "h3", "h4"}:
            text = element.get_text(" ", strip=True)
            return self._normalize_text(text)

        if element.name == "table":
            return self._table_to_text(element)

        return ""

    def _list_to_text(self, element) -> str:
        """
        Converte ul/ol in una lista markdown semplice.
        """
        items: list[str] = []
        seen_items: set[str] = set()

        for li in element.find_all("li", recursive=False):
            li_copy = BeautifulSoup(str(li), "html.parser")

            for nested_list in li_copy.find_all(["ul", "ol"]):
                nested_list.decompose()

            li_text = self._normalize_text(li_copy.get_text(" ", strip=True))
            if not li_text:
                continue
            if self._is_noise_line(li_text):
                continue
            if li_text in seen_items:
                continue

            seen_items.add(li_text)
            items.append(f"- {li_text}")

        return "\n".join(items).strip()

    def _table_to_text(self, table) -> str:
        """
        Converte una tabella Wikipedia in testo leggibile.

        Questo è fondamentale per pagine come liste di capitali, dove il contenuto
        principale è dentro wikitable / table.
        """
        classes = table.get("class", [])

        # Filtra tabelle quasi certamente decorative o di navigazione.
        noisy_table_classes = {
            "infobox",
            "sinottico",
            "navbox",
            "vertical-navbox",
            "metadata",
        }

        if any(cls in noisy_table_classes for cls in classes):
            return ""

        rows_output: list[str] = []
        seen_rows: set[str] = set()

        rows = table.find_all("tr", recursive=True)
        if not rows:
            return ""

        header_cells = rows[0].find_all(["th", "td"], recursive=False)
        header_texts = [
            self._normalize_text(cell.get_text(" ", strip=True))
            for cell in header_cells
        ]
        header_texts = [text for text in header_texts if text and not self._is_noise_line(text)]

        header_line = ""
        if header_texts and len(header_texts) <= 10:
            header_line = " | ".join(header_texts)

        if header_line and len(header_line) >= 3:
            rows_output.append(header_line)

        for row in rows[1:] if len(rows) > 1 else rows:
            cells = row.find_all(["th", "td"], recursive=False)
            if not cells:
                continue

            cell_texts: list[str] = []
            for cell in cells:
                for sup in cell.find_all("sup"):
                    sup.decompose()

                text = self._normalize_text(cell.get_text(" ", strip=True))
                if not text:
                    continue
                if self._is_noise_line(text):
                    continue
                cell_texts.append(text)

            if not cell_texts:
                continue

            row_line = " | ".join(cell_texts)
            row_line = self._normalize_text(row_line)

            if not row_line:
                continue
            if row_line in seen_rows:
                continue
            if len(row_line) < 3:
                continue

            seen_rows.add(row_line)
            rows_output.append(f"- {row_line}")

        if len(rows_output) <= 1 and not rows_output:
            return ""

        return "\n".join(rows_output).strip()

    def _normalize_text(self, text: str) -> str:
        """
        Normalizza spazi e piccoli artefatti.
        """
        text = re.sub(r"\[\d+\]", "", text)
        text = re.sub(r"\[[a-zA-Z]+\]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        text = text.replace(" ,", ",")
        text = text.replace(" .", ".")
        text = text.replace(" ;", ";")
        text = text.replace(" :", ":")
        text = text.replace(" ( ", " (")
        text = text.replace(" )", ")")
        text = text.strip("•· ")
        return text

    def _clean_heading(self, text: str) -> str:
        """
        Ripulisce heading Wikipedia.
        """
        text = self._normalize_text(text)
        text = text.replace("[modifica | modifica wikitesto]", "")
        text = text.replace("[modifica wikitesto]", "")
        text = text.strip(" -")
        return text.strip()

    def _is_noise_line(self, text: str) -> bool:
        """
        Filtra righe chiaramente non informative.
        """
        stripped = text.strip().lower()

        if not stripped:
            return True

        noise_exact = {
            "voci correlate",
            "collegamenti esterni",
            "altri progetti",
            "note",
            "bibliografia",
            "portale",
            "ricerca",
            "navigazione",
            "menu principale",
            "strumenti",
            "strumenti personali",
            "aspetto",
            "indice",
            "toc",
        }

        if stripped in noise_exact:
            return True

        noise_starts = [
            "vai al contenuto",
            "pagina principale",
            "ultime modifiche",
            "una voce a caso",
            "nelle vicinanze",
            "sportello informazioni",
            "pagine speciali",
            "fai una donazione",
            "registrati",
            "entra",
            "cookie",
            "privacy",
            "contribuisci",
            "scarica come pdf",
            "versione stampabile",
        ]

        noise_contains = [
            "modifica wikitesto",
            "sezione vuota",
            "questa voce o sezione",
            "aiutaci a scriverla",
        ]

        if any(stripped.startswith(prefix) for prefix in noise_starts):
            return True

        if any(fragment in stripped for fragment in noise_contains):
            return True

        return False

    def _post_process_blocks(self, blocks: list[str]) -> list[str]:
        """
        Ripulisce blocchi finali, rimuove vuoti e duplicati consecutivi o quasi inutili.
        """
        cleaned: list[str] = []
        seen: set[str] = set()
        previous = None

        for block in blocks:
            block = block.strip()
            if not block:
                continue

            block = re.sub(r"\n{3,}", "\n\n", block).strip()

            if block == previous:
                continue
            if block in seen:
                continue

            cleaned.append(block)
            seen.add(block)
            previous = block

        return cleaned

    def _cut_tail_sections(self, body: str) -> str:
        """
        Taglia le sezioni finali poco utili.
        """
        sections_to_cut = [
            "## Note",
            "## Bibliografia",
            "## Voci correlate",
            "## Collegamenti esterni",
            "## Altri progetti",
        ]

        cut_positions = []
        for section in sections_to_cut:
            pos = body.find(section)
            if pos != -1:
                cut_positions.append(pos)

        if cut_positions:
            body = body[:min(cut_positions)].strip()

        return body