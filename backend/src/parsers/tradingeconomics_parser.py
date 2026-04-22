import re
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.async_configs import CacheMode

try:
    from parsers.base_parser import BaseParser
except ModuleNotFoundError:
    from base_parser import BaseParser


class TradingEconomicsParser(BaseParser):
    """Parser per pagine TradingEconomics."""

    def __init__(self) -> None:
        self.browser_config = BrowserConfig(
            headless=True,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        )

        # Config live: più robusta per pagine dinamiche
        self.run_config_live = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            page_timeout=90000,
            delay_before_return_html=12.0,
            wait_until="networkidle",
            js_code="""
                const btn = Array.from(document.querySelectorAll('button'))
                    .find(b => /accept all/i.test(b.textContent.trim()));
                if (btn) { btn.click(); }
            """,
        )

        # Config html diretto: più leggera
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
            raise RuntimeError(
                f"Crawl fallito: {getattr(res, 'error_message', 'Errore sconosciuto')}"
            )

        title = self._estrai_titolo(res.markdown or "", res.html or "")
        parsed_text = self._pulisci_markdown(res.markdown or "")

        return {
            "url": url,
            "domain": domain,
            "title": title,
            "html_text": res.html or "",
            "parsed_text": parsed_text,
        }

    async def parse_from_html(self, url: str, html: str) -> dict:
        domain = urlparse(url).netloc

        # alleggerimento html per evitare rumore grafici/script
        html_clean = re.sub(
            r"<script\b[^>]*>.*?</script>",
            "",
            html,
            flags=re.DOTALL | re.IGNORECASE,
        )
        html_clean = re.sub(
            r"<iframe\b[^>]*>.*?</iframe>",
            "",
            html_clean,
            flags=re.DOTALL | re.IGNORECASE,
        )
        html_clean = re.sub(
            r'<div[^>]*(class|id)="[^"]*(chart|graph|highcharts)[^"]*"[^>]*>.*?</div>',
            "",
            html_clean,
            flags=re.DOTALL | re.IGNORECASE,
        )

        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            res = await crawler.arun(url=f"raw:{html_clean}", config=self.run_config_html)

        if not res.success:
            raise RuntimeError(
                f"Parse fallito: {getattr(res, 'error_message', 'Errore sconosciuto')}"
            )

        title = self._estrai_titolo(res.markdown or "", html_clean)
        parsed_text = self._pulisci_markdown(res.markdown or "")

        return {
            "url": url,
            "domain": domain,
            "title": title,
            "html_text": html,
            "parsed_text": parsed_text,
        }

    def _estrai_titolo(self, md: str, html: str = "") -> str:
        # priorità al tag <title>
        m = re.search(r"<title>\s*(.*?)\s*</title>", html, re.IGNORECASE | re.DOTALL)
        if m:
            title = re.sub(r"\s+", " ", m.group(1)).strip()
            title = re.sub(r"\s*\|\s*Trading Economics\s*$", "", title, flags=re.IGNORECASE)
            return title

        # fallback al primo header markdown
        m = re.search(r"^#\s+(.+)$", md, re.MULTILINE)
        if m:
            return m.group(1).strip()

        # fallback ulteriore
        m = re.search(r"^##\s+(.+)$", md, re.MULTILINE)
        return m.group(1).strip() if m else ""

    def _pulisci_markdown(self, md: str) -> str:
        if not md:
            return ""

        md = md.replace("\r\n", "\n").replace("\r", "\n")

        # 1) taglia testa/menu cercando un primo blocco "serio"
        inizio = re.search(r"^##\s+[A-Z].{10,}", md, re.MULTILINE)
        if inizio:
            md = md[inizio.start():]
        else:
            md = md.strip()

        # 2) taglia coda non utile
        fine = re.search(r"\nRelated\n|\nCompare:|\nNews Stream\n", md, flags=re.IGNORECASE)
        if fine:
            md = md[:fine.start()]

        match_cookie = re.search(r"Welcome to TRADING ECONOMICS", md, re.IGNORECASE)
        if match_cookie:
            md = md[:match_cookie.start()]

        # 3) se c'è blocco grafico prima della tabella, toglilo
        inizio_grafico = md.find("\n1D\n")
        inizio_tabella = md.find("Price    Day  Month  Year  Date")
        if inizio_grafico != -1 and inizio_tabella != -1 and inizio_grafico < inizio_tabella:
            md = md[:inizio_grafico] + md[inizio_tabella:]

        # 4) pulizia regex senza distruggere il Markdown
        substitutions = [
            (r"\[([^\]]+)\]\([^\)]+\)", r"\1"),     # link markdown -> testo
            (r"!\[[^\]]*\]\([^\)]*\)", ""),         # immagini markdown via
            (r"https?://\S+", ""),
            (r"(?m)^.*(Highcharts|Loading\.\.\.|Export API).*$", ""),
            (r"(?m)^\s*OK\s*$", ""),
            (r"(?m)^\s*\|?\s*World Bank[^\n]*$", ""),
            (r"(?m)^[\s\d]+Y[\s\d]*Y.*$", ""),
            (r"(?m)^(Compare:|USD Billion|points).*$", ""),
            (r"(?m)^\s*\|.*?GMT.*$", ""),
            (r"(?m)^\d{4}-\d{2}-\d{2}\s*\|.*$", ""),
            (r"(?m)^\s*more\s*$", ""),
            # etichette asse grafico
            (r"(?m)^(?:[A-Z][a-z]{2}){2,}\d*[A-Z]?[a-z]*\s*$", ""),
            # intestazione grafico
            (r"(?m)^\|.*?Value\s*Chg\s*Chg%.*$", ""),
            # cookie/privacy
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
        ]
        for pattern, repl in substitutions:
            md = re.sub(pattern, repl, md, flags=re.MULTILINE)

        # 5) filtro riga per riga
        linee = []
        for riga in md.splitlines():
            riga = riga.strip()

            if not riga:
                continue

            if any(x.lower() in riga.lower() for x in [
                "cookie duration",
                "data collected and processed:",
                "privacy policy",
                "storage details",
                "view details",
                "accept all",
                "confirm choices",
                "consentlegitimate interest",
                "legitimate interest",
                "doesn't use cookies",
                "uses other forms of storage",
            ]):
                continue

            # riga separatore tabella markdown vuota
            if re.match(r"^\|[\s\-\|]+$", riga):
                continue

            # tabelle markdown: tienile
            if riga.startswith("|") and len(riga) > 5:
                linee.append(riga)
                continue

            # righe brevissime non informative
            if len(riga) < 20 and not re.search(r"\d", riga):
                if re.match(r"^[A-Za-z\s%/,\-]+$", riga):
                    linee.append(riga)
                continue

            # solo numeri/simboli inutili
            if re.match(r"^[\d\s\.\,KMB\|\-]+$", riga):
                continue

            linee.append(riga)

        md = "\n".join(linee)

        # 6) pulizia finale mantenendo markdown
        md = re.sub(r"\n{3,}", "\n\n", md)
        md = re.sub(r"[ \t]{2,}", " ", md)
        md = "\n".join(line.strip() for line in md.splitlines())

        return md.strip()