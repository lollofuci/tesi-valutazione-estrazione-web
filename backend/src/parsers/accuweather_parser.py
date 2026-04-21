import re
from urllib.parse import urlparse, unquote

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from parsers.base_parser import BaseParser


class AccuWeatherParser(BaseParser):
    """Parser generale per pagine AccuWeather."""

    _START_PATTERNS = [
        r"##\s*Meteo attuale\b",
        r"##\s*Current Weather\b",
        r"##\s*Previsioni orarie\b",
        r"##\s*Hourly Weather\b",
        r"##\s*Previsioni giorno\b",
        r"##\s*Daily Weather\b",
        r"##\s*Sole e luna\b",
        r"##\s*Sun\s*&\s*Moon\b",
        r"##\s*Qualità dell'aria\b",
        r"##\s*Air Quality\b",
        r"##\s*Situazione allergie\b",
        r"##\s*Allergy Outlook\b",
    ]

    _STOP_PATTERNS = [
        r"©\s*\d{4}\s*AccuWeather,\s*Inc\.",
        r"^Condizioni di utilizzo\b",
        r"^Terms of Use\b",
        r"^Informativa sulla privacy\b",
        r"^Privacy Policy\b",
        r"^Norme sui cookie\b",
        r"^Cookie Policy\b",
        r"^Fonti dei dati\b",
        r"^Data Sources\b",
        r"^Around the Globe\b",
        r"^World\b",
        r"^Top Stories\b",
        r"^Featured Stories\b",
        r"^Weather News\b",
        r"^More Stories\b",
        r"^About AccuWeather\b",
        r"^Products\s*&\s*Services\b",
        r"^Proven Superior Accuracy\b",
    ]

    _NOISE_PATTERNS = [
        r"^Static Radar.*$",
        r"^Temporarily Unavailable.*$",
        r"^Thank you for your patience.*$",
        r"^Refresh Page\s*$",
        r"^Nuvole Temperatura\s*$",
        r"^Clouds Temperature\s*$",
        r"^Visualizza altro.*$",
        r"^See More.*$",
        r"^See All.*$",
        r"^Vedi tutto.*$",
        r"^Altri dettagli\s*$",
        r"^More Details\s*$",
        r"^Recent\s*$",
        r"^Go Back\s*$",
        r"^Use Current Location\s*$",
        r"^Chevron\s+(left|right)\s*$",
        r"^LEARN MORE\s*$",
        r"^No results found\.\s*$",
        r"^Try searching for.*$",
        r"^Dati non supportati in questa posizione\s*$",
        r"^Data not supported.*$",
        r"^Include informazioni Copernicus.*$",
        r"^Includes modified Copernicus.*$",
        r"^Advertisement\s*$",
        r"^Pubblicità\s*$",
    ]

    _KNOWN_HEADERS = [
        "Meteo attuale",
        "Current Weather",
        "Evoluzione",
        "Outlook",
        "Previsioni orarie",
        "Hourly Weather",
        "Previsioni giorno",
        "Daily Weather",
        "Sole e luna",
        "Sun & Moon",
        "Qualità dell'aria",
        "Air Quality",
        "Situazione allergie",
        "Allergy Outlook",
    ]

    def __init__(self) -> None:
        self.browser_config = BrowserConfig(headless=True)
        self.run_config = CrawlerRunConfig(
            word_count_threshold=1,
            remove_overlay_elements=True,
            exclude_social_media_links=True,
            process_iframes=False,
            css_selector="body",
        )

    async def parse(self, url: str) -> dict:
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            result = await crawler.arun(url=url, config=self.run_config)

        if not result.success:
            raise RuntimeError(
                f"Crawl fallito: {getattr(result, 'error_message', 'Errore sconosciuto')}"
            )

        return self._build_result(url, result.html, result.markdown)

    async def parse_from_html(self, url: str, html: str) -> dict:
        """Metodo lasciato disponibile, ma non usato dal parser eval."""
        raise NotImplementedError(
            "Per AccuWeather eval usa AccuWeatherEvalParser, non parse_from_html."
        )

    def _build_result(self, url: str, html: str, markdown: str) -> dict:
        domain = urlparse(url).netloc
        return {
            "url": url,
            "domain": domain,
            "title": self._extract_title(html, url),
            "html_text": html,
            "parsed_text": self._clean_markdown(markdown),
        }

    def _extract_title(self, html: str, url: str) -> str:
        match = re.search(r"<title>(.*?)</title>", html, flags=re.IGNORECASE | re.DOTALL)
        if match:
            title = re.sub(r"\s+", " ", match.group(1)).strip()
            title = re.sub(r"\s*\|\s*AccuWeather\s*$", "", title, flags=re.IGNORECASE)
            return title.strip()

        parts = [p for p in urlparse(url).path.split("/") if p]
        if len(parts) >= 3:
            return unquote(parts[2]).replace("-", " ").strip()

        return "accuweather"

    def _clean_markdown(self, md: str) -> str:
        md = md.replace("\r\n", "\n").replace("\r", "\n")

        md = re.sub(
            r"!\[(.*?)\]\((?:[^)(]+|\([^)(]*\))*\)",
            r"\1",
            md,
            flags=re.DOTALL,
        )
        md = re.sub(
            r"\[(.*?)\]\((?:[^)(]+|\([^)(]*\))*\)",
            r"\1",
            md,
            flags=re.DOTALL,
        )

        md = md.replace("**", "").replace("__", "").replace("*", "")

        for header in self._KNOWN_HEADERS:
            md = re.sub(
                rf"\s*(##\s*{re.escape(header)})\s*",
                r"\n\n\1\n",
                md,
            )

        start_regex = r"^(" + "|".join(self._START_PATTERNS) + r")"
        start_match = re.search(start_regex, md, flags=re.MULTILINE | re.IGNORECASE)
        if start_match:
            md = md[start_match.start():]

        stop_regex = r"(" + "|".join(self._STOP_PATTERNS) + r")"
        stop_match = re.search(stop_regex, md, flags=re.MULTILINE | re.IGNORECASE)
        if stop_match:
            md = md[:stop_match.start()]

        for pattern in self._NOISE_PATTERNS:
            md = re.sub(pattern, "", md, flags=re.MULTILINE | re.IGNORECASE)

        md = re.sub(r"\bRealFeel®?\s*\d+°", "", md, flags=re.IGNORECASE)
        md = re.sub(r"\bRealFeel Shade™?\s*\d+°", "", md, flags=re.IGNORECASE)
        md = re.sub(r"\bRealFeel Guide\b", "", md, flags=re.IGNORECASE)

        md = re.sub(r"[ \t]{2,}", " ", md)
        md = re.sub(r"\n[ \t]+", "\n", md)
        md = re.sub(r"[ \t]+\n", "\n", md)
        md = re.sub(r"\n{3,}", "\n\n", md)

        lines = []
        for line in md.splitlines():
            line = line.strip()
            if not line or line in {"#", "##", "###", "####"}:
                continue
            lines.append(line)

        return "\n".join(lines).strip()