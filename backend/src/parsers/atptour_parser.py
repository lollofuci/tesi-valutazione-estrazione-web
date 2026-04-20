import os
import re
import tempfile
import asyncio
from urllib.parse import urlparse, unquote

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from parsers.base_parser import BaseParser

class ATPTourParser(BaseParser):
    def __init__(self) -> None:
        self.browser_config = BrowserConfig(headless=True)
        self.run_config = CrawlerRunConfig(magic=True, cache_mode=CacheMode.BYPASS)

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

    def _smista_e_pulisci(self, url: str, md: str, titolo: str) -> str:
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
        md = re.sub(r"\r\n?", "\n", md)

        match_inizio = re.search(r"(?is)(?:Women's Tennis Association|ATP Fantasy|Gaming).*?Shop[^\w]*", md)
        if match_inizio:
            md = md[match_inizio.end():]
        else:
            match_inizio_2 = re.search(r"(?im)Shop[^\w]*", md)
            if match_inizio_2:
                md = md[match_inizio_2.end():]

        pattern_coda = r"(?is)(Riveting Rivalries|DOWNLOAD OFFICIAL|NEWSLETTERS|## Partners|#### Corporate|## Privacy Preference Center|Premier Partner|Related Players).*"
        match_bottom = re.search(pattern_coda, md)
        if match_bottom:
            md = md[:match_bottom.start()]

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

            if re.match(r"^[\s|:-]+$", s):
                continue
                
            s = s.replace("|", " ")
            s = re.sub(r"\s{2,}", " ", s).strip()

            s = re.sub(r"^(.*?)(YTD W/L|YTD titles|Career W/L|Career titles|Career prize money)(.*)$", r"\1\n\2\n\3", s)
            s = re.sub(r"^(Rank|Age|Weight|Height|Plays|Backhand|Turned Pro)(.*)$", r"\1\n\2", s)

            s_lower = s.lower()
            selettori_h2h = {"en", "es", "buy tickets", "search", "shop", "premier partner", "atp fantasy", "breakdown", "events breakdown"}
            if s_lower in selettori_h2h:
                continue
            
            if s_lower.startswith(("latest\nnews", "search icon", "filter icon", "related players")):
                continue

            for part in s.split('\n'):
                part = part.strip()
                if part:
                    linee_valide.append(part)

        testo_finale = "\n\n".join(linee_valide)
        testo_finale = re.sub(r"[ \t]{2,}", " ", testo_finale)
        return re.sub(r"\n{3,}", "\n\n", testo_finale).strip()