import os
import re
import tempfile
import asyncio
from urllib.parse import urlparse, unquote

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from parsers.base_parser import BaseParser


class ATPTourParser(BaseParser):
    """
    Parser UNIVERSALE per atptour.com basato sulla tecnica "Bottom Slice".
    Nessun selettore CSS: scarica l'intera pagina e isola il testo puro.
    """

    def __init__(self) -> None:
        self.browser_config = BrowserConfig(headless=False)
        self.run_config = CrawlerRunConfig(magic=True, cache_mode=CacheMode.BYPASS)

    async def parse_from_html(self, url: str, html: str) -> dict:
        domain = urlparse(url).netloc
        title = self._estrai_titolo_da_url(url)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".html", mode="w", encoding="utf-8") as tmp_file:
            tmp_file.write(html)
            tmp_file_path = tmp_file.name

        try:
            local_url = f"file:///{tmp_file_path.replace(os.sep, '/')}"

            async with AsyncWebCrawler(config=self.browser_config) as crawler:
                result = await crawler.arun(url=local_url, config=self.run_config)

            if not result.success:
                raise RuntimeError("Crawl fallito durante l'elaborazione dell'HTML offline.")

            raw_markdown = result.markdown or ""
            parsed_text = self._smista_e_pulisci(url, raw_markdown, title)

        finally:
            if os.path.exists(tmp_file_path):
                os.remove(tmp_file_path)

        return {
            "url": url,
            "domain": domain,
            "title": title,
            "html_text": html,
            "parsed_text": parsed_text,
        }

    async def parse(self, url: str) -> dict:
        domain = urlparse(url).netloc
        title = self._estrai_titolo_da_url(url)

        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            result = await crawler.arun(url=url, config=self.run_config)

        if not result.success:
            error_message = getattr(result, "error_message", "Errore sconosciuto")
            raise RuntimeError(f"Crawl fallito: {error_message}")

        raw_html = result.html or ""
        raw_markdown = result.markdown or ""

        parsed_text = self._smista_e_pulisci(url, raw_markdown, title)

        return {
            "url": url,
            "domain": domain,
            "title": title,
            "html_text": raw_html,
            "parsed_text": parsed_text,
        }

    def _estrai_titolo_da_url(self, url: str) -> str:
        path_parts = urlparse(url).path.strip("/").split("/")
        slug = path_parts[-1]
        if len(slug) < 5 and slug.isupper() and len(path_parts) > 1:
            slug = path_parts[-3] if "vs" in path_parts[-3] else path_parts[-2]
        slug = unquote(slug).replace("-", " ")
        return slug.title().strip()

    # ==========================================
    # ROUTER E METODI DI PULIZIA SPECIFICI
    # ==========================================
    
    def _smista_e_pulisci(self, url: str, md: str, titolo: str) -> str:
        """Legge l'URL e decide quali 'forbici' usare per tagliare il Markdown."""
        if "/news/" in url:
            return self._pulisci_news(md, titolo)
        elif "/atp-head-2-head/" in url or "/head-2-head/" in url:
            return self._pulisci_h2h(md, titolo)
        else:
            return self._pulisci_news(md, titolo) 

    def _pulisci_news(self, md: str, titolo: str) -> str:
        md = re.sub(r"\r\n?", "\n", md)

        match_inizio = re.search(r"(?im)^\s*\*\s*Email\s*\n(Match Report\s*\n)?", md)
        if match_inizio:
            md = md[match_inizio.end():]
        else:
            parole_titolo = titolo.split()
            if len(parole_titolo) >= 2:
                inizio_titolo = f"{parole_titolo[0]} {parole_titolo[1]}"
                match_titolo = re.search(rf"(?im)^{re.escape(inizio_titolo)}", md)
                if match_titolo:
                    md = md[match_titolo.start():]

        pattern_coda = r"(?ms)^(###\s+(Read More News|View Related|Stats widget|DOWNLOAD)|## Header 2|NEWSLETTERS|## Partners|#### Corporate|## Privacy Preference Center).*$"
        match_bottom = re.search(pattern_coda, md)
        if match_bottom:
            md = md[:match_bottom.start()]

        md = re.sub(r"(?is)Video Player is loading\..*?(?:Close Modal Dialog|End of dialog window\.|Reset restore all settings to the default valuesDone)", "", md)
        md = re.sub(r"(?mi)^(Close Modal Dialog|End of dialog window\.|This is a modal window\..*?)\s*$", "", md)

        linee_valide = []
        for line in md.splitlines():
            s = line.strip()
            if not s: continue

            s = re.sub(r"\[\]\([^)]+\)", "", s)
            s = re.sub(r"!\[.*?\]\([^)]+\)", "", s)
            s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
            s = s.lstrip("#* ").strip()
            
            if not s: continue

            if re.match(r"^(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}$", s):
                continue

            s_lower = s.lower()
            selettori_spazzatura = {
                "share", "play", "mute", "chapters", "getty images", "/", "1x", "done",
                "match report", "play video", "audio track", "descriptions", "captions",
                "picture-in-picturefullscreen", "en", "es", "close modal dialog", "end of dialog window." 
            }
            if s_lower in selettori_spazzatura: continue
            if s_lower.startswith((
                "descriptions off", "captions settings", "captions off", "text colorwhite", "background color", "window color",
                "font size", "text edge", "font family", "reset restore", "current time", "duration", "loaded:", "stream type", "seek to live",
                "remaining time", "playback rate", "beginning of dialog window", "this is a modal window" 
            )): continue

            linee_valide.append(s)

        testo_finale = "\n\n".join(linee_valide)
        testo_finale = re.sub(r"[ \t]{2,}", " ", testo_finale)
        return re.sub(r"\n{3,}", "\n\n", testo_finale).strip()


    def _pulisci_h2h(self, md: str, titolo: str) -> str:
        """Nuova logica ultra-precisa per le pagine Head-2-Head."""
        md = re.sub(r"\r\n?", "\n", md)

        # 1. TAGLIO TESTA H2H: Il menu finisce con "Shop", seguito da dei punti esclamativi "!"
        # Questa regex taglia tutto fino all'ultimo "!" del menu.
        match_inizio = re.search(r"(?im)^Shop\s*\n+(?:!\s*\n*)*", md)
        if match_inizio:
            md = md[match_inizio.end():]

        # 2. TAGLIO CODA H2H: Tagliamo via i widget "Riveting Rivalries" e l'App
        pattern_coda = r"(?ms)^(Riveting Rivalries|DOWNLOAD OFFICIAL|NEWSLETTERS|## Partners|#### Corporate|## Privacy Preference Center).*$"
        match_bottom = re.search(pattern_coda, md)
        if match_bottom:
            md = md[:match_bottom.start()]

        # 3. PULIZIA RIGA PER RIGA (Rimozione tabelle e rumore)
        linee_valide = []
        for line in md.splitlines():
            s = line.strip()
            if not s: continue

            # Rimuoviamo immagini e puliamo i link testuali
            s = re.sub(r"\[\]\([^)]+\)", "", s)
            s = re.sub(r"!\[.*?\]\([^)]+\)", "", s)
            s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
            s = s.lstrip("#* ").strip()
            
            if not s: continue

            # Distrugge la riga di formattazione delle tabelle Markdown (es. | --- | --- |)
            if re.match(r"^[\s|:-]+$", s):
                continue
                
            # Sostituisce le "pipe" (|) della tabella con spazi, rendendolo testo semplice come vuoi tu
            s = s.replace("|", " ")
            s = re.sub(r"\s{2,}", " ", s).strip()

            s_lower = s.lower()
            
            # Parole spazzatura specifiche che ATP inserisce nell'H2H e che non ci servono
            selettori_h2h = {"en", "es", "buy tickets", "search", "breakdown", "events breakdown"}
            if s_lower in selettori_h2h:
                continue
            
            # Filtri di inizio riga per rimuovere le icone non caricate
            if s_lower.startswith(("latest\nnews", "search icon", "filter icon")):
                continue

            linee_valide.append(s)

        testo_finale = "\n\n".join(linee_valide)
        testo_finale = re.sub(r"[ \t]{2,}", " ", testo_finale)
        return re.sub(r"\n{3,}", "\n\n", testo_finale).strip()