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

        for element in root_copy.find_all(
            ["h2", "h3", "h4", "p", "ul", "ol", "dl"],
            recursive=True,
        ):
            text = self._element_to_text(element)
            if not text:
                continue

            if self._is_noise_line(text):
                continue

            if element.name in {"h2", "h3", "h4"}:
                heading = self._clean_heading(text)
                if heading:
                    level = {"h2": "##", "h3": "###", "h4": "####"}[element.name]
                    blocks.append(f"{level} {heading}")
            else:
                blocks.append(text)

        return blocks

    def _extract_visible_text_lines(self, soup: BeautifulSoup) -> list[str]:
        """
        Ultimo fallback: prende il testo visibile globale della pagina.
        """
        body = soup.body or soup
        text = body.get_text("\n", strip=True)
        lines = [self._normalize_text(line) for line in text.splitlines()]

        cleaned_lines: list[str] = []
        for line in lines:
            if not line:
                continue
            if len(line) < 25:
                continue
            if self._is_noise_line(line):
                continue
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
            items = []
            for li in element.find_all("li", recursive=False):
                li_text = self._normalize_text(li.get_text(" ", strip=True))
                if li_text and not self._is_noise_line(li_text):
                    items.append(f"- {li_text}")
            return "\n".join(items).strip()

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

        return ""

    def _normalize_text(self, text: str) -> str:
        """
        Normalizza spazi e piccoli artefatti.
        """
        text = re.sub(r"\[\d+\]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        text = text.replace(" ,", ",")
        text = text.replace(" .", ".")
        text = text.replace(" ;", ";")
        text = text.replace(" :", ":")
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
        ]

        return any(stripped.startswith(prefix) for prefix in noise_starts)

    def _post_process_blocks(self, blocks: list[str]) -> list[str]:
        """
        Ripulisce blocchi finali, rimuove vuoti e duplicati consecutivi.
        """
        cleaned: list[str] = []
        previous = None

        for block in blocks:
            block = block.strip()
            if not block:
                continue
            if block == previous:
                continue
            cleaned.append(block)
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