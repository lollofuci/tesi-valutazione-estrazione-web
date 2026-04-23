import re
from urllib.parse import urlparse, unquote

from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

from parsers.base_parser import BaseParser


class WikipediaParser(BaseParser):
    """Parser dedicato alle pagine Wikipedia."""

    def __init__(self) -> None:
        self.browser_config = BrowserConfig(headless=True)

        # Per il parsing live della pagina vera
        self.run_config_live = CrawlerRunConfig(css_selector="#mw-content-text")

    async def parse(self, url: str) -> dict:
        """
        Parsing live: usa Crawl4AI sulla pagina vera.
        """
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            result = await crawler.arun(url=url, config=self.run_config_live)

        if not result.success:
            error_message = getattr(result, "error_message", "Errore sconosciuto")
            raise RuntimeError(f"Crawl fallito: {error_message}")

        domain = urlparse(url).netloc
        title = self._extract_title_from_url(url)

        parsed_text = self._clean_live_markdown(result.markdown or "", title)

        return {
            "url": url,
            "domain": domain,
            "title": title,
            "html_text": result.html or "",
            "parsed_text": parsed_text,
        }

    async def parse_from_html(self, url: str, html: str) -> dict:
        """
        Parsing da html_text del GS: usa BeautifulSoup direttamente.
        """
        domain = urlparse(url).netloc
        title = self._extract_title_from_url(url)

        parsed_text = self._extract_markdown_from_html(html, title)

        return {
            "url": url,
            "domain": domain,
            "title": title,
            "html_text": html,
            "parsed_text": parsed_text,
        }

    def _extract_title_from_url(self, url: str) -> str:
        slug = urlparse(url).path.split("/wiki/")[-1]
        slug = re.sub(r"_\(.*?\)", "", slug)
        return unquote(slug).replace("_", " ").strip()

    # -------------------------
    # PATH LIVE (Crawl4AI)
    # -------------------------

    def _clean_live_markdown(self, md: str, title: str) -> str:
        md = self.clean_markdown(md)

        # Link markdown -> solo testo
        md = re.sub(r"\[\[(.*?)\]\((?:[^)(]+|\([^)(]*\))*\)", r"\1", md)
        md = re.sub(r"\[(.*?)\]\((?:[^)(]+|\([^)(]*\))*\)", r"\1", md)

        # Taglia le sezioni finali meno utili
        md = re.sub(
            r"(?ms)^##\s+(Note|Bibliografia|Voci correlate|Altri progetti|Collegamenti esterni|Categorie|Fonti).*",
            "",
            md,
        )

        sostituzioni = [
            (r"(?i)Questa voce o sezione.*?\.", ""),
            (r"(?i)Commento\s*:.*", ""),
            (r"\s*\([^)]*AFI:[^)]*\)", ""),
            (r"ascoltaⓘ", ""),
            (r"pronunciaⓘ", ""),
            (r"(?i)!\[.*?\]\(.*?\)", ""),
            (r"(?im)^.*?\.(jpg|jpeg|png|svg|webp|pdf|gif).*?$", ""),
            (r"\[modifica\s*\|\s*modifica wikitesto\]", ""),
            (r"\[\s*nota\s*\d+(?:\s*,\s*\d+)*\s*\]", ""),
            (r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]", ""),
            (r"Coordinate:.*", ""),
            (r"Da Wikipedia, l'enciclopedia libera\.", ""),
            (r"Lo stesso argomento in dettaglio:.*", ""),
            (r"\\\(", "("),
            (r"\\\)", ")"),
            (r"(?m)^\s*\*\s*\*\s*\*\s*$", ""),
        ]

        for pattern, repl in sostituzioni:
            md = re.sub(pattern, repl, md, flags=re.IGNORECASE)

        md = re.sub(r"[ \t]{2,}", " ", md)
        md = re.sub(r"\n{3,}", "\n\n", md)
        md = md.strip()

        if md and not md.startswith("#"):
            md = f"# {title}\n\n{md}"

        return md.strip()

    # -------------------------
    # PATH GS HTML (BeautifulSoup)
    # -------------------------

    def _extract_markdown_from_html(self, html: str, title: str) -> str:
        soup = BeautifulSoup(html, "html.parser")

        content = (
            soup.select_one("#mw-content-text")
            or soup.select_one("#bodyContent")
            or soup.select_one("main")
            or soup.body
            or soup
        )

        selectors_to_remove = [
            ".navbox",
            ".vertical-navbox",
            ".metadata",
            ".infobox",
            ".ambox",
            ".tmbox",
            ".toc",
            ".mw-editsection",
            ".reflist",
            ".reference",
            ".references",
            ".thumb",
            ".sidebar",
            ".hatnote",
            ".sistersitebox",
            ".noprint",
            "style",
            "script",
            "sup.reference",
        ]

        for selector in selectors_to_remove:
            for tag in content.select(selector):
                tag.decompose()

        blocks = [f"# {title}"]

        allowed_tags = {"h2", "h3", "p", "ul", "ol", "table"}

        stop_sections = {
            "note",
            "bibliografia",
            "voci correlate",
            "altri progetti",
            "collegamenti esterni",
            "fonti",
            "references",
            "external links",
            "see also",
            "further reading",
            "bibliography",
        }

        stop_mode = False

        for node in content.find_all(allowed_tags):
            if stop_mode:
                break

            name = node.name.lower()

            if name == "h2":
                heading = self._clean_text(node.get_text(" ", strip=True))
                if not heading:
                    continue

                if heading.lower() in stop_sections:
                    stop_mode = True
                    break

                blocks.append(f"## {heading}")

            elif name == "h3":
                heading = self._clean_text(node.get_text(" ", strip=True))
                if heading:
                    blocks.append(f"### {heading}")

            elif name == "p":
                text = self._clean_text(node.get_text(" ", strip=True))
                if self._is_good_paragraph(text):
                    blocks.append(text)

            elif name in {"ul", "ol"}:
                for li in node.find_all("li", recursive=False):
                    text = self._clean_text(li.get_text(" ", strip=True))
                    if self._is_good_list_item(text):
                        blocks.append(f"- {text}")

            elif name == "table":
                classes = node.get("class", [])
                if "wikitable" in classes:
                    table_md = self._table_to_markdown(node)
                    if table_md:
                        blocks.append(table_md)

        md = "\n\n".join(blocks)
        md = re.sub(r"\n{3,}", "\n\n", md).strip()

        return md

    def _table_to_markdown(self, table) -> str:
        rows = []

        for tr in table.find_all("tr"):
            cells = tr.find_all(["th", "td"], recursive=False)
            if not cells:
                continue

            row = []
            for cell in cells:
                text = self._clean_text(cell.get_text(" ", strip=True))
                text = text.replace("|", "/")
                if text:
                    row.append(text)

            if row:
                rows.append(row)

        if not rows:
            return ""

        max_cols = max(len(row) for row in rows)
        normalized_rows = []

        for row in rows:
            padded = row + [""] * (max_cols - len(row))
            normalized_rows.append(padded)

        header = normalized_rows[0]
        separator = ["---"] * max_cols

        md_lines = [
            "| " + " | ".join(header) + " |",
            "| " + " | ".join(separator) + " |",
        ]

        for row in normalized_rows[1:]:
            md_lines.append("| " + " | ".join(row) + " |")

        return "\n".join(md_lines).strip()

    def _clean_text(self, text: str) -> str:
        text = text.replace("\xa0", " ")
        text = re.sub(r"\[modifica\s*\|\s*modifica wikitesto\]", "", text, flags=re.I)
        text = re.sub(r"\[\s*nota\s*\d+(?:\s*,\s*\d+)*\s*\]", "", text, flags=re.I)
        text = re.sub(r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]", "", text)
        text = re.sub(r"Da Wikipedia, l'enciclopedia libera\.", "", text, flags=re.I)
        text = re.sub(r"Questa voce o sezione.*?\.", "", text, flags=re.I)
        text = re.sub(r"Lo stesso argomento in dettaglio:.*", "", text, flags=re.I)
        text = re.sub(r"Coordinate:.*", "", text, flags=re.I)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def _is_good_paragraph(self, text: str) -> bool:
        if not text:
            return False

        low = text.lower()

        bad_prefixes = (
            "questa voce o sezione",
            "lo stesso argomento in dettaglio",
            "coordinate:",
            "da wikipedia",
        )
        if low.startswith(bad_prefixes):
            return False

        if len(text) < 25:
            return False

        return True

    def _is_good_list_item(self, text: str) -> bool:
        if not text:
            return False
        if len(text) < 8:
            return False
        return True