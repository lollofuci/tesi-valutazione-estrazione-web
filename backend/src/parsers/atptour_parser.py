import re
import html as html_lib
from urllib.parse import urlparse, unquote
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from parsers.base_parser import BaseParser

class ATPTourParser(BaseParser):
    def __init__(self) -> None:
        self.browser_config = BrowserConfig(headless=True,headers={"User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) ""AppleWebKit/537.36 (KHTML, like Gecko) ""Chrome/122.0.0.0 Safari/537.36"),"Accept-Language": "en-US,en;q=0.9",},)
        self.run_config = CrawlerRunConfig(magic=False,cache_mode=CacheMode.BYPASS,page_timeout=120000,delay_before_return_html=5.0)

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

    async def parse_from_html(self, url: str, html_text: str) -> dict:
        domain = urlparse(url).netloc
        title = self._estrai_titolo_da_url(url)

        text = self._html_to_text_offline(html_text)
        parsed_text = self._smista_e_pulisci(url, text, title)

        return {
            "url": url,
            "domain": domain,
            "title": title,
            "html_text": html_text,
            "parsed_text": parsed_text,
        }

    def _html_to_text_offline(self, html_content: str) -> str:
        text = html_content
        text = re.sub(r"<script\b[^>]*>.*?</script>", "", text, flags=re.IGNORECASE | re.DOTALL)
        text = re.sub(r"<style\b[^>]*>.*?</style>", "", text, flags=re.IGNORECASE | re.DOTALL)
        text = re.sub(r"<h1\b[^>]*>", "\n# ", text, flags=re.IGNORECASE)
        text = re.sub(r"<h2\b[^>]*>", "\n## ", text, flags=re.IGNORECASE)
        text = re.sub(r"<h3\b[^>]*>", "\n### ", text, flags=re.IGNORECASE)
        text = re.sub(r"</h[1-6]>", "\n", text, flags=re.IGNORECASE)
        text = re.sub(r"</?(br|hr)\b[^>]*>", "\n", text, flags=re.IGNORECASE)
        text = re.sub(r"</?(p|div|section|article|main|aside|header|footer|li|ul|ol|span|table|tr|td|th)\b[^>]*>", "\n", text, flags=re.IGNORECASE)
        text = re.sub(r"<[^>]+>", " ", text)
        text = html_lib.unescape(text)
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n[ \t]+", "\n", text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)

        lines = []
        for raw_line in text.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            low = line.lower()
            garbage_prefixes = ("cookie", "privacy", "terms", "accept", "search", "shop", "buy tickets", "more navigation links", "header 2")
            if low.startswith(garbage_prefixes):
                continue
            lines.append(line)

        return "\n".join(lines).strip()

    def _estrai_titolo_da_url(self, url: str) -> str:
        path_parts = urlparse(url).path.strip("/").split("/")
        if "players" in path_parts:
            idx = path_parts.index("players")
            if idx + 1 < len(path_parts):
                return unquote(path_parts[idx + 1]).replace("-", " ").title().strip()
        if "atp-head-2-head" in path_parts:
            slug = path_parts[-3] if len(path_parts) >= 3 else path_parts[-1]
        else:
            slug = path_parts[-1]
        slug = unquote(slug).replace("-", " ")
        return slug.title().strip()

    def _smista_e_pulisci(self, url: str, md: str, titolo: str) -> str:
        md = self.clean_markdown(md)
        if "/news" in url:
            return self._pulisci_news(md, titolo)
        if "/atp-head-2-head" in url or "/head-2-head" in url:
            return self._pulisci_h2h(md, titolo)
        if "/players/" in url:
            return self._pulisci_player(md, titolo)
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
            if not s:
                continue
            s = re.sub(r"!\[.*?\]\([^)]+\)", "", s)
            s = re.sub(r"\[?\s*\]\([^)]+\)", "", s)
            s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
            if not s:
                continue
            if re.match(r"^(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}$", s):
                continue
            s_lower = s.replace("#", "").replace("*", "").strip().lower()
            selettori_spazzatura = {"share", "play", "mute", "chapters", "getty images", "/", "1x", "done", "match report", "play video", "audio track", "descriptions", "captions", "picture-in-picturefullscreen", "en", "es", "close modal dialog", "end of dialog window.", "shop", "premier partner"}
            if s_lower in selettori_spazzatura:
                continue
            if s_lower.startswith(("descriptions off", "captions settings", "captions off", "text colorwhite", "background color", "window color", "font size", "text edge", "font family", "reset restore", "current time", "duration", "loaded:", "stream type", "seek to live", "remaining time", "playback rate", "beginning of dialog window", "this is a modal window")):
                continue
            linee_valide.append(s)

        testo_finale = "\n\n".join(linee_valide)
        testo_finale = re.sub(r"[ \t]{2,}", " ", testo_finale)
        testo_finale = re.sub(r"\n{3,}", "\n\n", testo_finale).strip()

        if testo_finale and not testo_finale.startswith("#"):
            testo_finale = f"# {titolo}\n\n{testo_finale}"
        return testo_finale

    def _pulisci_h2h(self, md: str, titolo: str) -> str:
        md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)
        md = re.sub(r"!\[.*?\]\([^)]+\)", "", md)
        lines = [line.strip() for line in md.splitlines() if line.strip()]

        start_idx = 0
        end_idx = len(lines)

        voci_menu = {"gaming", "atp fantasy", "shop", "shop !"}
        for i, line in enumerate(lines):
            if line.replace("#", "").replace("*", "").strip().lower() in voci_menu:
                start_idx = i + 1

        voci_coda = ("riveting rivalries", "download official", "privacy preference center", "related players", "view all", "partners", "newsletters", "fierce feuds", "corporate", "media", "related links")
        for i in range(start_idx, len(lines)):
            l_clean = lines[i].replace("#", "").replace("*", "").strip().lower()
            if l_clean.startswith(voci_coda) or l_clean in voci_coda:
                end_idx = i
                break

        risultato = []
        garbage = {"en", "es", "buy tickets", "search", "shop", "premier partner", "atp fantasy", "gaming", "breakdown", "events breakdown", "players", "players home", "atp coach members", "header 2"}

        for i in range(start_idx, end_idx):
            s = lines[i].replace("*", "").replace("#", "").replace("!", "").strip()
            if not s or re.match(r"^[\s\|\:\-]+$", s):
                continue
            s = re.sub(r"player-photo-[a-z0-9]+", "", s, flags=re.IGNORECASE)
            s = s.replace("|", "\t")
            s = re.sub(r"\s{2,}", " ", s).strip()
            s_low = s.lower()
            if s_low in garbage:
                continue
            if s_low.startswith(("latest news", "search icon", "filter icon", "related players")):
                continue
            match_stats = re.match(r"^([\d/,\$\.-]+)\s*(YTD W/L|YTD titles|Career W/L|Career titles|Career prize money)\s*([\d/,\$\.-]+)$", s, re.IGNORECASE)
            if match_stats:
                val1, label, val2 = match_stats.groups()
                risultato.append(val1.strip())
                risultato.append(label.strip())
                risultato.append(val2.strip())
                continue
            match_bio = re.match(r"^(Rank|Age|Weight|Height|Plays|Backhand|Turned Pro)(.*)$", s, re.IGNORECASE)
            if match_bio:
                label, val = match_bio.groups()
                risultato.append(label.strip())
                if val.strip():
                    risultato.append(val.strip())
                continue
            if s_low.startswith(("year\twinner", "202", "199", "198")):
                s = s.replace("\t", " ")
                risultato.append(s)
                continue
            risultato.append(s)

        if not risultato:
            return f"# {titolo}\n\nDati non trovati."
        if len(risultato) > 4:
            if risultato[0].lower() == titolo.lower() and risultato[1].lower() == titolo.lower():
                risultato = risultato[1:]
        if not risultato[0].startswith("#"):
            risultato[0] = f"# {risultato[0]}"
        return "\n".join(risultato).strip()

    def _pulisci_player(self, md: str, titolo: str) -> str:
        md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)
        md = re.sub(r"!\[.*?\]\([^)]+\)", "", md)
        md = md.replace("\r\n", "\n")
        lines = [line.strip() for line in md.splitlines() if line.strip()]

        start_idx = 0
        end_idx = len(lines)

        for i, line in enumerate(lines):
            l_clean = line.lower().replace("*", "").replace("#", "").strip()
            if l_clean == "ytd" or l_clean.startswith("ytd "):
                for j in range(i, max(-1, i - 10), -1):
                    prev_clean = lines[j].lower().replace("*", "").replace("#", "").strip()
                    if titolo.lower() in prev_clean:
                        start_idx = j
                        break
                else:
                    start_idx = max(0, i - 2)
                break
        else:
            for i in range(len(lines)):
                if titolo.lower() in lines[i].lower():
                    start_idx = i
                    break

        voci_coda = ["latest news", "editor's picks", "last event played", "see more player", "newsletters", "corporate", "privacy preference center", "related players", "search opponent"]
        for i in range(start_idx + 5, len(lines)):
            l_clean = lines[i].lower().replace("*", "").replace("#", "").strip()
            if any(l_clean.startswith(vc) for vc in voci_coda) or l_clean in voci_coda:
                end_idx = i
                break

        risultato = []
        garbage = {"en", "es", "buy tickets", "search", "shop", "premier partner", "atp fantasy", "gaming", "players", "players home", "atp coach members", "overview", "bio", "activity", "stats", "ranking", "facebook", "x", "tiktok", "email", "header 2", "more navigation links", "vs", "insta"}
        titolo_low = titolo.lower()

        for i in range(start_idx, end_idx):
            s = lines[i].replace("*", "").replace("#", "").replace("!", "").strip()
            if not s or re.match(r"^[\s\|\:\-]+$", s):
                continue
            s_low = s.lower()
            if s_low in garbage:
                continue
            if s_low.startswith(("headshot-", "filter icon", "search icon", "ytd rank:")):
                continue
            if s_low == titolo_low and len(risultato) > 0:
                continue
            s = re.sub(r"^(Age|Weight|Height|Turned pro|Country|Birthplace|Plays|Coach)(.*)$", r"\1\n\2", s, flags=re.IGNORECASE)
            for part in s.split("\n"):
                p = part.strip()
                if p:
                    risultato.append(p)

        if not risultato:
            return f"# {titolo}\n\nDati non trovati."
        if not risultato[0].startswith("#"):
            risultato[0] = f"# {risultato[0]}"
        return "\n".join(risultato).strip()