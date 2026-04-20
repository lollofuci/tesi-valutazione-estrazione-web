import re
from urllib.parse import urlparse, unquote

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

from parsers.base_parser import BaseParser


class WikipediaParser(BaseParser):
    """Parser dedicato alle pagine Wikipedia."""

    def __init__(self) -> None:
        self.browser_config = BrowserConfig(headless=True)
        self.run_config = CrawlerRunConfig(css_selector="#bodyContent")

    async def parse(self, url: str) -> dict:
        """
        Scarica la pagina dall'URL e delega il parsing a parse_from_html.
        """
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            result = await crawler.arun(url=url, config=self.run_config)

        if not result.success:
            error_message = getattr(result, "error_message", "Errore sconosciuto")
            raise RuntimeError(f"Crawl fallito: {error_message}")

        parsed_result = await self.parse_from_html(url, result.html)

        # Se vuoi continuare a usare il markdown prodotto da Crawl4AI,
        # puoi sovrascrivere parsed_text con quello pulito da result.markdown.
        parsed_result["parsed_text"] = self._pulisci_markdown(result.markdown, url)

        return parsed_result

    async def parse_from_html(self, url: str, html: str) -> dict:
        """
        Dato un URL e l'HTML grezzo, restituisce i dati parsati.
        """
        domain = urlparse(url).netloc
        title = self._estrai_titolo_da_url(url)

        return {
            "url": url,
            "domain": domain,
            "title": title,
            "html_text": html,
            "parsed_text": "",  # verrà valorizzato in parse()
        }

    def _estrai_titolo_da_url(self, url: str) -> str:
        slug = urlparse(url).path.split("/wiki/")[-1]
        slug = re.sub(r"_\(.*?\)", "", slug)
        return unquote(slug).replace("_", " ").strip()

    def _pulisci_markdown(self, md: str, url: str) -> str:
        titolo = self._estrai_titolo_da_url(url)

        match_def = re.search(rf"(?mi)\*\*{re.escape(titolo)}.*?\*\*", md)
        if match_def:
            inizio = md.rfind("\n", 0, match_def.start())
            md = md[inizio if inizio != -1 else match_def.start():]
        else:
            match_generic = re.search(r"(?mi)^\s*\*\*.*?\*\*\s*\(", md)
            if match_generic:
                md = md[match_generic.start():]

        md = re.sub(
            r"(?ms)^##\s+(Note|Bibliografia|Voci correlate|Altri progetti|Collegamenti esterni|Categorie|Note e progetti|Fonti).*",
            "",
            md,
        )

        sostituzioni = [
            (r"\[\[(.*?)\]\]\((?:[^)(]+|\([^)(]*\))*\)", r"\1"),
            (r"\[(.*?)\]\((?:[^)(]+|\([^)(]*\))*\)", r"\1"),
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
            (r"\*\*", ""),
            (r"_", ""),
            (r"\\\(", "("),
            (r"\\\)", ")"),
            (r"(?m)^\s*\*\s*\*\s*\*\s*$", ""),
        ]

        for pattern, repl in sostituzioni:
            md = re.sub(pattern, repl, md, flags=re.IGNORECASE)

        md = re.sub(r"(?<=[A-Za-zÀ-ÖØ-öø-ÿ])\d+\b", "", md)
        md = re.sub(r"\b\d+(?=[,.;:!?])", "", md)

        linee_pulite = []
        for line in md.splitlines():
            s = line.strip()

            if not s:
                continue

            if s.startswith('|') or s.startswith('+-') or (s.count('|') > 1):
                linee_pulite.append(line)
                continue

            if s.startswith(('*', '-', '1.', '#')):
                linee_pulite.append(line)
                continue

            if len(s) < 30 and not re.search(
                r"\b(è|sono|fu|era|si trova|ospita|rappresenta|nato|morto)\b", s, re.I
            ):
                if not s.endswith((".", ":", ";")):
                    continue

            linee_pulite.append(line)

        md = "\n".join(linee_pulite)
        md = re.sub(r"[ \t]{2,}", " ", md)
        md = re.sub(r"\n{3,}", "\n\n", md)

        return md.strip()