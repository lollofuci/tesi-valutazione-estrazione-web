import re
from urllib.parse import urlparse, unquote

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

from parsers.base_parser import BaseParser


class WikipediaParserClean(BaseParser):
    """Parser Wikipedia con pulizia lato crawler."""

    def __init__(self) -> None:
        self.browser_config = BrowserConfig(headless=True)

        self.run_config = CrawlerRunConfig(
        css_selector="#bodyContent",
        excluded_tags=[
            "table",
            "figure",
            "img",
            "aside",
            "style",
            "script",
            "noscript",
        ],
        excluded_selector="""
            .infobox,
            .navbox,
            .vertical-navbox,
            .toc,
            .mw-editsection,
            .metadata,
            .ambox,
            .reflist,
            .reference,
            .references,
            .sidebar,
            .thumb,
            .gallery
        """,
    )

    async def parse(self, url: str) -> dict:
        domain = urlparse(url).netloc
        title = self._extract_title_from_url(url)

        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            result = await crawler.arun(url=url, config=self.run_config)

        if not result.success:
            error_message = getattr(result, "error_message", "Errore sconosciuto")
            raise RuntimeError(f"Crawl fallito: {error_message}")

        parsed_text = self._clean_markdown(result.markdown)

        return {
            "url": url,
            "domain": domain,
            "title": title,
            "html_text": result.html,
            "parsed_text": parsed_text,
        }

    def _extract_title_from_url(self, url: str) -> str:
        slug = urlparse(url).path.split("/wiki/")[-1]
        return unquote(slug).replace("_", " ").strip()

    def _clean_markdown(self, md: str) -> str:
        """Pulizia leggera del markdown già filtrato dal crawler."""

        md = re.sub(
            r"(?ms)^##\s+(Note|Bibliografia|Voci correlate|Altri progetti|Collegamenti esterni|Categorie).*",
            "",
            md,
        )

        patterns = [
            r"(?im)^Da Wikipedia, l'enciclopedia libera\.\s*$",
            r"(?im)^Coordinate:.*$",
            r"(?im)^Lo stesso argomento in dettaglio:.*$",
        ]

        for pattern in patterns:
            md = re.sub(pattern, "", md)

        md = re.sub(r"!\[.*?\]\(.*?\)", "", md)
        md = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", md)
        md = re.sub(r"\*\*", "", md)

        lines = []
        for line in md.splitlines():
            s = line.strip()
            if not s:
                continue
            lines.append(s)

        md = "\n".join(lines)
        md = re.sub(r"\n{3,}", "\n\n", md)

        return md.strip()