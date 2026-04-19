import re
from urllib.parse import urlparse
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.async_configs import CacheMode

try:
    from parsers.base_parser import BaseParser
except ModuleNotFoundError:
    from base_parser import BaseParser


class TradingEconomicsParser(BaseParser):

    def __init__(self) -> None:
        self.browser_config = BrowserConfig(
            headless=True,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        self.run_config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            page_timeout=60000,
            delay_before_return_html=6.0,
            wait_until="networkidle",
            
        )

    async def parse(self, url: str) -> dict:
        domain = urlparse(url).netloc
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            res = await crawler.arun(url=url, config=self.run_config)
        if not res.success:
            raise RuntimeError(f"Crawl fallito: {getattr(res, 'error_message', 'Errore sconosciuto')}")
        return {
            "url": url,
            "domain": domain,
            "title": self._estrai_titolo(res.markdown),
            "html_text": res.html,
            "parsed_text": self._pulisci_markdown(res.markdown),
        }

    def _estrai_titolo(self, md: str) -> str:
        """Estrae il titolo dal primo heading # (es. 'Italy GDP')."""
        m = re.search(r"^# (.+)$", md, re.MULTILINE)
        return m.group(1).strip() if m else ""

    def _pulisci_markdown(self, md: str) -> str:
        # 1) Taglia testa (menu)
        md_originale = md
        inizio = re.search(r"^## [A-Z].{20,}", md, re.MULTILINE)
        if not inizio:
            return md.strip()
        md = md[inizio.start():]

        # 2) Taglia coda — più aggressivo, prende il primo match
        fine = re.search(r"\nRelated\n|\n\*\*[A-Z]|\nCompare:", md)
        if fine:
            md = md[:fine.start()]
        titolo = self._estrai_titolo(md_originale)
        if titolo:
            md = re.sub(rf"(?m)^{re.escape(titolo)}\s*$", "", md)


        # 3) Pulizia regex
        for pattern, repl in [
            (r"(?m)^#{1,6}\s+", ""),
            (r"\[([^\]]+)\]\(https?://[^\)]+\)", r"\1"),
            (r"!\[[^\]]*\]\([^\)]*\)", ""),
            (r"https?://\S+", ""),
            (r"(?m)source:\s*[^\n]*", ""),
            (r"(?m)^.*(Highcharts|Loading\.\.\.|Export API).*$", ""),
            (r"(?m)^\s*OK\s*$", ""),
            (r"(?m)^\s*\|?\s*World Bank[^\n]*$", ""),
            (r"(?m)^[\s\d]+Y[\s\d]*Y.*$", ""),
            (r"(?m)^(Compare:|USD Billion|points).*$", ""),
            (r"(?m)^\s*\|.*?GMT.*$", ""),
            (r"(?m)^\d{4}-\d{2}-\d{2}\s*\|.*$", ""),
            (r"(?m)^\s*more\s*$", ""),
            (r"\*\*.*?\*\*", ""),
            # Etichette asse X del grafico (mesi+anno attaccati es. MayJulSepNov2026Mar)
            (r"(?m)^(?:[A-Z][a-z]{2}){2,}\d*[A-Z]?[a-z]*\s*$", ""),

            # Intestazione grafico con nome ente + ValueChgChg%
            (r"(?m)^\|.*?Value\s*Chg\s*Chg%.*$", ""),

            # FIX righe calendario con ora (11:00 AM)
            (r"(?m)^\|?\s*\d{4}-\d{2}-\d{2}.*$", "")
        ]:
            md = re.sub(pattern, repl, md, flags=re.MULTILINE)

        # 4) Filtraggio riga per riga
        linee = []
        for riga in md.splitlines():
            s = riga.strip()
            if not s:
                continue
            if re.match(r"^\|[\s\-\|]+$", s):
                continue
            if s.startswith("|") and len(s) > 5:
                linee.append(s)
                continue
            if len(s) < 20 and not re.search(r"\d", s):
                continue
            if re.match(r"^[\d\s\.\,KMB\|\-]+$", s):
                continue
            linee.append(riga)

        md = "\n".join(linee)
        md = re.sub(r"\n{3,}", "\n\n", md)
        md = re.sub(r"[ \t]{2,}", " ", md)
        return md.strip()
    async def parse_from_html(self, url: str, html: str) -> dict:
        domain = urlparse(url).netloc
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            res = await crawler.arun(url=f"raw://{html}", config=self.run_config)
        if not res.success:
            raise RuntimeError("Parse fallito")
        return {
            "url": url,
            "domain": domain,
            "title": self._estrai_titolo(res.markdown),
            "parsed_text": self._pulisci_markdown(res.markdown),
        }