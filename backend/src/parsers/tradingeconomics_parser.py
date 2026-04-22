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
        self.run_config_live = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            page_timeout=90000,
            delay_before_return_html=12.0,
            wait_until="networkidle",
            js_code="""
                const btn = Array.from(document.querySelectorAll('button'))
                    .find(b => b.textContent.trim() === 'Accept all');
                if (btn) { btn.click(); }
            """,
         )
        self.run_config_html = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            page_timeout=90000,
            delay_before_return_html=0.5,
            wait_until="domcontentloaded",
        )
    async def parse(self, url: str) -> dict:
        
        domain = urlparse(url).netloc
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            res = await crawler.arun(url=url, config=self.run_config_live)
        if not res.success:
            raise RuntimeError(f"Crawl fallito: {getattr(res, 'error_message', 'Errore sconosciuto')}")
        return {
             "url": url,
             "domain": domain,
             "title": self._estrai_titolo(res.markdown),
             "html_text": res.html,
             "parsed_text": self._pulisci_markdown(res.markdown),
        }

    def _estrai_titolo(self, md: str,html: str="") -> str:
        m = re.search(r"<title>\s*(.*?)\s*</title>", html, re.IGNORECASE | re.DOTALL)
        if m:
            return m.group(1).strip()

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

        match_cookie = re.search(r"Welcome to TRADING ECONOMICS", md, re.IGNORECASE)
        if match_cookie:
            md = md[:match_cookie.start()]
        inizio_grafico = md.find("\n1D\n")
        inizio_tabella = md.find("Price    Day  Month  Year  Date")

        if inizio_grafico != -1 and inizio_tabella != -1 and inizio_grafico < inizio_tabella:
            md = md[:inizio_grafico] + md[inizio_tabella:]

        pos_news_stream = md.find("News Stream")
        if pos_news_stream != -1:
            md = md[:pos_news_stream]
            


        # 3) Pulizia regex
        for pattern, repl in [
            (r"(?m)^#{1,6}\s+", ""),
            (r"\[([^\]]+)\]\([^\)]+\)", r"\1"),
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
            (r"(?m)^\|?\s*\d{4}-\d{2}-\d{2}.*$", ""),
            (r"(?mi)^.*Cookie duration.*$", ""),
            (r"(?mi)^.*Data collected and processed:.*$", ""),
            (r"(?mi)^.*Privacy policy.*$", ""),
            (r"(?mi)^.*Storage details.*$", ""),
            (r"(?mi)^.*View details.*$", ""),
            (r"(?mi)^.*Accept all.*$", ""),
            (r"(?mi)^.*Confirm choices.*$", ""),
            (r"(?mi)^.*Close\s*$", ""),
            (r"(?mi)^.*ConsentLegitimate interest.*$", ""),
            (r"(?mi)^.*Legitimate interest.*$", ""),
            (r"(?mi)^.*Doesn't use cookies.*$", ""),
            (r"(?mi)^.*Uses other forms of storage.*$", ""),
        ]:
            md = re.sub(pattern, repl, md, flags=re.MULTILINE)

        # 4) Filtraggio riga per riga
        linee = []
        for riga in md.splitlines():
            riga = riga.strip()
            if any(x in riga for x in [
                "Cookie duration",
                "Data collected and processed:",
                "Privacy policy",
                "Storage details",
                "View details",
                "Accept all",
                "Confirm choices",
                "ConsentLegitimate interest",
                "Legitimate interest",
                "Doesn't use cookies",
                "Uses other forms of storage",
            ]):
                continue
            if not riga:
                continue
            if re.match(r"^\|[\s\-\|]+$", riga):
                continue
            if riga.startswith("|") and len(riga) > 5:
                linee.append(riga)
                continue
            if len(riga) < 20 and not re.search(r"\d", riga):
                if re.match(r"^[A-Za-z\s]+$", riga):  
                    linee.append(riga)
                continue
            if re.match(r"^[\d\s\.\,KMB\|\-]+$", riga):
                continue
            
            linee.append(riga)

        md = "\n".join(linee)
        md = re.sub(r"\n{3,}", "\n\n", md)
        md = re.sub(r"[ \t]{2,}", " ", md)
        md = md.replace("|", "")  
        md = "\n".join(line.strip() for line in md.splitlines())  
        return md.strip()
    async def parse_from_html(self, url: str, html: str) -> dict:
        domain = urlparse(url).netloc
        html = re.sub(r"<script\b[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
        html = re.sub(r"<iframe\b[^>]*>.*?</iframe>", "", html, flags=re.DOTALL | re.IGNORECASE)
        html = re.sub(
            r'<div[^>]*(class|id)="[^"]*(chart|graph|highcharts)[^"]*"[^>]*>.*?</div>',
            "",
            html,
            flags=re.DOTALL | re.IGNORECASE
        )
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            res = await crawler.arun(url=f"raw://{html}", config=self.run_config_html)
        if not res.success:
            raise RuntimeError("Parse fallito")
        return {
            "url": url,
            "domain": domain,
            "title": self._estrai_titolo(res.markdown),
            "html_text":html,
            "parsed_text": self._pulisci_markdown(res.markdown),
        }
    



