import re
from urllib.parse import urlparse
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.async_configs import CacheMode
from parsers.base_parser import BaseParser


class TradingEconomicsParser(BaseParser):

    def __init__(self) -> None:
        self.browser_config = BrowserConfig(headless=True, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        self.run_config_live = CrawlerRunConfig(cache_mode=CacheMode.BYPASS,page_timeout=90000,delay_before_return_html=12.0,wait_until="networkidle",    js_code="""
        const btn = document.querySelector('button#onetrust-accept-btn-handler') 
            || document.querySelector('button.accept-cookies')
            || document.querySelector('[id*="accept"]');
        if (btn) btn.click();
    """)
        self.run_config_html = CrawlerRunConfig(cache_mode=CacheMode.BYPASS,delay_before_return_html=0.5,wait_until="domcontentloaded")
        
        
    async def parse(self, url: str) -> dict:
        domain = urlparse(url).netloc
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            res = await crawler.arun(url=url, config=self.run_config_live)
        if not res.success:
            raise RuntimeError(f"Crawl fallito: {getattr(res, 'error_message', 'Errore sconosciuto')}")
        return {
             "url": url,
             "domain": domain,
             "title": self._estrai_titolo(res.markdown, res.html),
             "html_text": res.html,
             "parsed_text": self._pulisci_markdown(res.markdown),
        }

    def _estrai_titolo(self, md: str, html: str="") -> str:
        if html:
            m = re.search(r"<title>\s*(.*?)\s*</title>", html, re.IGNORECASE | re.DOTALL)
            if m:
                return m.group(1).strip()

        m = re.search(r"^# (.+)$", md, re.MULTILINE)
        return m.group(1).strip() if m else "Trading Economics"

    def _pulisci_markdown(self, md: str) -> str:
        if not md: return ""
        
        inizio = re.search(r"^## [A-Z].{20,}", md, re.MULTILINE)
        if not inizio:
            return md.strip()
        md = md[inizio.start():]

        fine = re.search(r"\nRelated\n|\n\*\*[A-Z]|\nCompare:", md)
        if fine:
            md = md[:fine.start()]

        match_cookie = re.search(r"Welcome to TRADING ECONOMICS", md, re.IGNORECASE)
        if match_cookie:
            md = md[:match_cookie.start()]
        
        md = re.sub(r"\n1D\s*\nCompare\s*\nExport\s*\nAPI.*?\nSubmit\s*\nPrice\s+Day\s+Month\s+Year\s+Date","\nPrice    Day  Month  Year  Date",md,flags=re.DOTALL)
        pos_news_stream = md.find("News Stream")
        if pos_news_stream != -1:
            md = md[:pos_news_stream]
            
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
            (r"(?m)^(?:[A-Z][a-z]{2}){2,}\d*[A-Z]?[a-z]*\s*$", ""),
            (r"(?m)^\|.*?Value\s*Chg\s*Chg%.*$", ""),
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
            (r"(?s)Crude Oil fell to .*?was last updated on April \d{1,2} of \d{4}\.", ""),
            (r"(?s)Crude Oil fell to .*?Looking forward, we estimate it to trade at .*?12 months time\.", ""),
            (r"(?m)^Dec\d{4}.*$", ""),
            (r"(?s)GDP in Italy averaged .*?was last updated on April of \d{4}\.", ""),
            (r"(?s)GDP in Italy is expected to reach .*?according to our econometric models\.", ""),
            (r"(?s)GDP in [A-Z][A-Za-z\s]+ averaged .*?was last updated on April of \d{4}\.", ""),
            (r"(?s)GDP in [A-Z][A-Za-z\s]+ is expected to reach .*?according to our econometric models\.", ""),
            (r"(?m)^\d+(?:\.\d+)?K\s+USD Billion\s*$", ""),
        ]:
            md = re.sub(pattern, repl, md, flags=re.MULTILINE)

        linee = []
        for riga in md.splitlines():
            riga = riga.strip()
            if riga in {"1D", "Compare", "Export", "API", "Crude Oil X", "LNR", "Submit", "1D1W1M6M1Y5Y10Y25YAll"}:
                continue
            if riga.startswith("Crude Oil WTI (USD/Bbl)"):
                continue
            if riga.startswith("Intraday1 Minute5 Minutes"):
                continue
            if riga.startswith("[](#)"):
                continue
            if re.match(r"^[A-Z][a-z]{2}\s+\d{1,2}\s+\d{4}$", riga):
                continue
            if re.match(r"^\d+(?:\.\d+)?$", riga):
                continue
            if any(x in riga for x in ["Cookie duration","Data collected and processed:","Privacy policy","Storage details","View details","Accept all","Confirm choices","ConsentLegitimate interest","Legitimate interest","Doesn't use cookies","Uses other forms of storage"]):
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
            linee.append(riga)

        md = "\n".join(linee)
        md = re.sub(r"\n{3,}", "\n\n", md)
        md = re.sub(r"[ \t]{2,}", " ", md)
        md = md.replace("|", "")  
        md = "\n".join(line.strip() for line in md.splitlines())  
        return md.strip()

    async def parse_from_html(self, url: str, html: str) -> dict:
        from bs4 import BeautifulSoup
        import gc

        domain = urlparse(url).netloc
        soup = BeautifulSoup(html, "html.parser")

        tables = soup.find_all("table", class_=lambda c: c and "table-heatmap" in c)

        if tables and "/commodity/" not in url:
            rows = []
            for table in tables:
                header = table.find("thead")
                if header:
                    cols = [th.get_text(strip=True) for th in header.find_all("th")]
                    rows.append("\t".join(cols))
                for tr in table.find("tbody").find_all("tr"):
                    cells = [td.get_text(strip=True) for td in tr.find_all("td")]
                    rows.append("\t".join(cells))
            parsed_text = "\n".join(rows)
        else:
            clean_html = re.sub(r"<script\b[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
            clean_html = re.sub(r"<iframe\b[^>]*>.*?</iframe>", "", clean_html, flags=re.DOTALL | re.IGNORECASE)
            async with AsyncWebCrawler(config=self.browser_config) as crawler:
                res = await crawler.arun(url=f"raw:{clean_html}", config=self.run_config_html)
            if not res.success:
                raise RuntimeError("Parse fallito")
            parsed_text = self._pulisci_markdown(res.markdown or "")

        gc.collect()

        return {
            "url": url,
            "domain": domain,
            "title": self._estrai_titolo("", html),
            "html_text": html,
            "parsed_text": parsed_text,
        }