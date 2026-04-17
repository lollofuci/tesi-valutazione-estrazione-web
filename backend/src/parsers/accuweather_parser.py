import re
from urllib.parse import urlparse, unquote

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

from parsers.base_parser import BaseParser


class AccuWeatherParser(BaseParser):
    """Parser semplice e generale per pagine AccuWeather."""

    def __init__(self) -> None:
        self.browser_config = BrowserConfig(headless=True)

        # prendiamo il contenuto centrale della pagina, non tutta la pagina
        self.run_config = CrawlerRunConfig(
            word_count_threshold=1,
            remove_overlay_elements=True,
            exclude_external_links=False,
            exclude_social_media_links=True,
            process_iframes=False,
            css_selector="body",
        )

    async def parse(self, url: str) -> dict:
        domain = urlparse(url).netloc

        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            result = await crawler.arun(url=url, config=self.run_config)

        if not result.success:
            error_message = getattr(result, "error_message", "Errore sconosciuto")
            raise RuntimeError(f"Crawl fallito: {error_message}")

        return {
            "url": url,
            "domain": domain,
            "title": self._estrai_titolo(result.html, url),
            "html_text": result.html,
            "parsed_text": self._pulisci_markdown(result.markdown),
        }

    def _estrai_titolo(self, html: str, url: str) -> str:
        match = re.search(r"<title>(.*?)</title>", html, flags=re.I | re.S)
        if match:
            title = match.group(1).strip()
            title = re.sub(r"\s*\|\s*AccuWeather\s*$", "", title, flags=re.I)
            return title

        parts = [p for p in urlparse(url).path.split("/") if p]
        if len(parts) >= 3:
            return unquote(parts[2]).replace("-", " ").strip()

        return "accuweather"

    def _pulisci_markdown(self, md: str) -> str:
        md = md.replace("\r\n", "\n").replace("\r", "\n")

        # 1. immagini markdown -> tieni solo l'alt text
        md = re.sub(
            r"!\[(.*?)\]\((?:[^)(]+|\([^)(]*\))*\)",
            r"\1",
            md,
            flags=re.DOTALL,
        )

        # 2. link markdown -> tieni solo il testo
        md = re.sub(
            r"\[(.*?)\]\((?:[^)(]+|\([^)(]*\))*\)",
            r"\1",
            md,
            flags=re.DOTALL,
        )

        # 3. pulizia markdown base
        md = re.sub(r"\*\*", "", md)
        md = re.sub(r"_", " ", md)

        # 4. parti dal primo blocco meteo serio
        start_match = re.search(
            r"(?mi)^(#\s*Current Weather|##\s*Current Weather|##\s*Today's Weather|##\s*Day|##\s*Night|##\s*Hourly Weather|##\s*10-Day Weather Forecast|##\s*Air Quality)",
            md,
        )
        if start_match:
            md = md[start_match.start():]

        # 5. togli solo rumore chiarissimo
        rumore = [
            r"(?mi)^Today Hourly 10-Day Radar MinuteCast® Monthly Air Quality Health & Activities\s*$",
            r"(?mi)^Go Back\s*$",
            r"(?mi)^Use Current Location\s*$",
            r"(?mi)^Recent\s*$",
            r"(?mi)^See More\s*$",
            r"(?mi)^See All\s*$",
            r"(?mi)^Refresh Page\s*$",
            r"(?mi)^Chevron left\s*$",
            r"(?mi)^Chevron right\s*$",
            r"(?mi)^LEARN MORE\s*$",
            r"(?mi)^Further Ahead\s*$",
            r"(?mi)^RealFeel Guide\s*$",
            r"(?mi)^No results found\.\s*$",
            r"(?mi)^Try searching for a city, zip code or point of interest\.\s*$",
        ]

        for pattern in rumore:
            md = re.sub(pattern, "", md)

        # 6. taglia quando iniziano davvero blocchi non utili / finali
        stop_match = re.search(
            r"(?mi)^("
            r"###\s*Hourly\s*###\s*10-Day\s*###\s*Monthly|"
            r"Around the Globe|"
            r"###\s*Hurricane\s*###\s*Severe Weather\s*###\s*Radar\s*&\s*Maps\s*###\s*News\s*###\s*Video|"
            r"Top Stories|"
            r"Featured Stories|"
            r"Weather News|"
            r"More Stories|"
            r"About AccuWeather|"
            r"Products\s*&\s*Services|"
            r"Subscription Services|"
            r"Weather Near|"
            r"Proven Superior Accuracy™|"
            r"World\s+Europe"
            r")\b",
            md,
        )
        if stop_match:
            md = md[:stop_match.start()]

        # 7. etichette fastidiose ma non informative
        md = re.sub(r"\bMore Details\b", "", md, flags=re.I)
        md = re.sub(r"\bRealFeel Guide\b", "", md, flags=re.I)

        # 8. normalizzazione
        md = re.sub(r"[ \t]{2,}", " ", md)
        md = re.sub(r"\n{3,}", "\n\n", md)

        # 9. togli righe vuote / segnaposto inutili
        linee_pulite = []
        for line in md.splitlines():
            s = line.strip()

            if not s:
                continue

            if s in {"#", "##", "###"}:
                continue

            linee_pulite.append(s)

        return "\n".join(linee_pulite).strip()