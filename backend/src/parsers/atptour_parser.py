import os
import re
import tempfile
import asyncio
from urllib.parse import urlparse, unquote

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from parsers.base_parser import BaseParser

class ATPTourParser(BaseParser):
    def __init__(self) -> None:
        self.browser_config = BrowserConfig(
            headless=False, # Lascialo a False per non far scattare l'antibot!
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9"
            }
        )
        self.run_config = CrawlerRunConfig(
            magic=True, 
            cache_mode=CacheMode.BYPASS,
            page_timeout=60000,
            delay_before_return_html=3.0  # Tempo vitale per far caricare i numeri reali al sito
        )

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
            
            # ATTENZIONE QUI: Passiamo 'html' (il codice sorgente originale) direttamente allo smistatore!
            parsed_text = self._smista_e_pulisci(url, raw_markdown, title, html)

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

        # Passiamo raw_html al pulitore
        parsed_text = self._smista_e_pulisci(url, raw_markdown, title, raw_html)

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

    def _smista_e_pulisci(self, url: str, md: str, titolo: str, html: str = "") -> str:
        # Aggiornato per includere l'HTML diretto nei player
        if "/news" in url:
            return self._pulisci_news(md, titolo)
        elif "/atp-head-2-head" in url or "/head-2-head" in url:
            return self._pulisci_h2h(md, titolo)
        elif "/players/" in url:
            return self._pulisci_player(html, titolo) # Svolta epocale: usiamo l'HTML puro!
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

        pattern_coda = r"(?ms)^(###\s+(Read More News|View Related|Stats widget|DOWNLOAD)|## Header 2|NEWSLETTERS|## Partners|#### Corporate|## Privacy Preference Center|Premier Partner).*$"
        match_bottom = re.search(pattern_coda, md)
        if match_bottom:
            md = md[:match_bottom.start()]

        md = re.sub(r"(?is)Video Player is loading\..*?(?:Close Modal Dialog|End of dialog window\.|Reset restore all settings to the default valuesDone)", "", md)
        md = re.sub(r"(?mi)^(Close Modal Dialog|End of dialog window\.|This is a modal window\..*?)\s*$", "", md)

        linee_valide = []
        for line in md.splitlines():
            s = line.strip()
            if not s: continue

            s = re.sub(r"!\[.*?\]\([^)]+\)", "", s)
            s = re.sub(r"\[?\s*\]\([^)]+\)", "", s)
            s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
            s = s.replace("[", "").replace("]", "")
            s = s.lstrip("#* ").strip("! ")
            
            if not s: continue

            if re.match(r"^(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}$", s):
                continue

            s_lower = s.lower()
            selettori_spazzatura = {
                "share", "play", "mute", "chapters", "getty images", "/", "1x", "done",
                "match report", "play video", "audio track", "descriptions", "captions",
                "picture-in-picturefullscreen", "en", "es", "close modal dialog", "end of dialog window.",
                "shop", "premier partner"
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
        md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md) 
        md = re.sub(r"!\[.*?\]\([^)]+\)", "", md)

        lines = [line.strip() for line in md.splitlines() if line.strip()]

        start_idx = 0
        end_idx = len(lines)

        voci_menu = {"gaming", "atp fantasy", "women's tennis association", "shop", "shop !"}
        for i, line in enumerate(lines):
            if line.lower() in voci_menu:
                start_idx = i + 1

        voci_coda = ("riveting rivalries", "download official", "privacy preference center", "related players", "view all", "## partners", "newsletters", "fierce feuds")
        for i in range(start_idx, len(lines)):
            if lines[i].lower().startswith(voci_coda):
                end_idx = i
                break

        linee_valide = []
        for i in range(start_idx, end_idx):
            s = lines[i]
            s = s.replace("[", "").replace("]", "").replace("!", "").strip()

            if re.match(r"^[\s\|\:\-]+$", s):
                continue
            
            s = s.replace("|", " ")
            s = re.sub(r"\s{2,}", " ", s).strip()

            s_low = s.lower()
            if s_low in {"en", "es", "buy tickets", "search", "shop", "premier partner", "atp fantasy", "gaming", "breakdown", "events breakdown"}:
                continue
            if s_low.startswith(("latest news", "search icon", "filter icon", "related players")):
                continue

            s = re.sub(r"^(.*?)(YTD W/L|YTD titles|Career W/L|Career titles|Career prize money)(.*)$", r"\1\n\2\n\3", s)
            s = re.sub(r"^(Rank|Age|Weight|Height|Plays|Backhand|Turned Pro)(.*)$", r"\1\n\2", s)

            for part in s.split('\n'):
                p = part.strip()
                if p: linee_valide.append(p)

        return "\n\n".join(linee_valide).strip()

    def _pulisci_player(self, html: str, titolo: str) -> str:
        """La soluzione definitiva: estrae i dati ignorando completamente il Markdown."""
        if not html: 
            return titolo
        
        # Eliminiamo blocchi pesanti e script
        html_clean = re.sub(r'<(script|style|svg|noscript|form|nav|footer)[^>]*>.*?</\1>', ' ', html, flags=re.DOTALL | re.IGNORECASE)
        
        # Isola il blocco YTD / Career (Statistiche)
        stats_match = re.search(r'<div class="atp_player-stats".*?(?=<div class="player_image|<div class="atp_info-ribbon|<div class="atp_player-personaldetails")', html_clean, flags=re.DOTALL | re.IGNORECASE)
        stats_html = stats_match.group(0) if stats_match else ""
        
        # Isola il blocco Personal Details (Età, Peso, ecc.)
        pd_match = re.search(r'<div class="atp_player-personaldetails".*?(?=<div class="atp_player-latest-news"|<div class="atp_head2head)', html_clean, flags=re.DOTALL | re.IGNORECASE)
        pd_html = pd_match.group(0) if pd_match else ""
        
        target_html = stats_html + "\n" + pd_html
        
        # Trasforma l'HTML rimasto in testo puro inserendo 'a capo' al posto dei tag
        testo_grezzo = re.sub(r'<[^>]+>', '\n', target_html)
        
        # Pulisce gli spazi e le righe vuote
        lines = [line.strip() for line in testo_grezzo.split('\n') if line.strip()]
        
        risultato = [titolo]
        garbage = {"singles", "doubles", "header 2", "follow player", "insta", "x", "facebook", "tiktok"}
        
        for line in lines:
            l_low = line.lower()
            if l_low in garbage or "atp no.1 club" in l_low:
                continue
            if "${" in line: # Filtro di sicurezza contro scarti di codice
                continue
            if l_low == titolo.lower():
                continue
            
            risultato.append(line)

        # Magia finale: unisce i numeri alle etichette (Es. "1" e "Rank" diventano "1 Rank")
        labels = {"Rank", "Move", "W-L", "Titles", "Prize Money", "Prize Money Singles & Doubles Combined", "Career High Rank"}
        
        final_lines = []
        for item in risultato:
            is_label = any(item.startswith(lbl) for lbl in labels)
            # Se è una label, la attacca al numero precedente!
            if is_label and final_lines and not final_lines[-1].startswith(("YTD", "Career")):
                final_lines[-1] = final_lines[-1] + " " + item
            else:
                final_lines.append(item)

        if len(final_lines) <= 1:
            return titolo + "\n\nDati non trovati nel DOM HTML."

        # Reinserisce "Personal details" nel posto giusto per estetica
        if "Age" in final_lines:
            idx = final_lines.index("Age")
            final_lines.insert(idx, "Personal details")

        return "\n".join(final_lines)