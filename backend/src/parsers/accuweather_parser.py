import re
import html as html_lib
from urllib.parse import urlparse, unquote
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from parsers.base_parser import BaseParser

class AccuWeatherParser(BaseParser):
    def __init__(self) -> None:
        self.browser_config = BrowserConfig(headless=True)
        self.run_config = CrawlerRunConfig(word_count_threshold=1,remove_overlay_elements=True,exclude_social_media_links=True,process_iframes=False,css_selector="body")

    async def parse(self, url: str) -> dict:
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            result = await crawler.arun(url=url, config=self.run_config)

        if not result.success:
            raise RuntimeError(f"Crawl fallito: {getattr(result, 'error_message', 'Errore sconosciuto')}")

        html = result.html or ""
        base_text = self._prepare_markdown_text(result.markdown or "")
        return self._build_result(url, html, base_text)

    async def parse_from_html(self, url: str, html: str) -> dict:
        base_text = self._html_to_text(html)
        return self._build_result(url, html, base_text)

    def _build_result(self, url: str, html: str, base_text: str) -> dict:
        domain = urlparse(url).netloc
        title = self._extract_title(html, url)
        parsed_text = self._parse_accuweather_text(base_text, title, url)
        return {
            "url": url,
            "domain": domain,
            "title": title,
            "html_text": html,
            "parsed_text": parsed_text,
        }

    def _extract_title(self, html: str, url: str) -> str:
        match = re.search(r"<title>(.*?)</title>", html, flags=re.IGNORECASE | re.DOTALL)
        if match:
            title = re.sub(r"\s+", " ", match.group(1)).strip()
            title = re.sub(r"\s*\|\s*AccuWeather\s*$", "", title, flags=re.IGNORECASE)
            return title.strip()
        parts = [p for p in urlparse(url).path.split("/") if p]
        if len(parts) >= 3:
            city = unquote(parts[2]).replace("-", " ").strip()
            if city:
                return city
        return "accuweather"

    def _prepare_markdown_text(self, md: str) -> str:
        md = self.clean_markdown(md)
        md = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", md)
        md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)

        replacements = [
            (r"(?mi)^\s*METEO ATTUALE\s*$", "## METEO ATTUALE"),
            (r"(?mi)^\s*CURRENT WEATHER\s*$", "## CURRENT WEATHER"),
            (r"(?mi)^\s*EVOLUZIONE\s*$", "## EVOLUZIONE"),
            (r"(?mi)^\s*OUTLOOK\s*$", "## OUTLOOK"),
            (r"(?mi)^\s*PREVISIONI ORARIE\s*$", "## PREVISIONI ORARIE"),
            (r"(?mi)^\s*HOURLY WEATHER\s*$", "## HOURLY WEATHER"),
            (r"(?mi)^\s*PREVISIONI GIORNO\s*$", "## PREVISIONI GIORNO"),
            (r"(?mi)^\s*DAILY WEATHER\s*$", "## DAILY WEATHER"),
            (r"(?mi)^\s*SOLE E LUNA\s*$", "## SOLE E LUNA"),
            (r"(?mi)^\s*SUN\s*&\s*MOON\s*$", "## SUN & MOON"),
            (r"(?mi)^\s*QUALITÀ DELL'ARIA\s*$", "## QUALITÀ DELL'ARIA"),
            (r"(?mi)^\s*AIR QUALITY\s*$", "## AIR QUALITY"),
            (r"(?mi)^\s*SITUAZIONE ALLERGIE\s*$", "## SITUAZIONE ALLERGIE"),
            (r"(?mi)^\s*ALLERGY OUTLOOK\s*$", "## ALLERGY OUTLOOK"),
            (r"(?mi)^\s*TONIGHT'?S WEATHER\s*$", "## TONIGHT'S WEATHER"),
        ]
        for pattern, repl in replacements:
            md = re.sub(pattern, repl, md)
        return md.strip()

    def _html_to_text(self, html: str) -> str:
        text = html
        text = re.sub(r"<script\b[^>]*>.*?</script>", "", text, flags=re.IGNORECASE | re.DOTALL)
        text = re.sub(r"<style\b[^>]*>.*?</style>", "", text, flags=re.IGNORECASE | re.DOTALL)
        text = re.sub(r"<h1\b[^>]*>", "\n# ", text, flags=re.IGNORECASE)
        text = re.sub(r"<h2\b[^>]*>", "\n## ", text, flags=re.IGNORECASE)
        text = re.sub(r"<h3\b[^>]*>", "\n### ", text, flags=re.IGNORECASE)
        text = re.sub(r"</h[1-6]>", "\n", text, flags=re.IGNORECASE)
        text = re.sub(r"</?(br|hr)\b[^>]*>", "\n", text, flags=re.IGNORECASE)
        text = re.sub(r"</?(p|div|section|article|main|aside|header|footer|li|ul|ol|span)\b[^>]*>", "\n", text, flags=re.IGNORECASE)
        text = re.sub(r"<[^>]+>", " ", text)
        text = html_lib.unescape(text)
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n[ \t]+", "\n", text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return self._prepare_markdown_text(text)

    def _extract_section(self, text: str, start_patterns: list[str], stop_patterns: list[str]) -> str:
        start = None
        for pat in start_patterns:
            m = re.search(pat, text, flags=re.IGNORECASE | re.MULTILINE)
            if m and (start is None or m.start() < start[0]):
                start = (m.start(), m.end())

        if start is None:
            return ""

        start_pos = start[0]
        end_pos = len(text)

        for pat in stop_patterns:
            m = re.search(pat, text[start_pos + 1:], flags=re.IGNORECASE | re.MULTILINE)
            if m:
                candidate_end = start_pos + 1 + m.start()
                if candidate_end < end_pos:
                    end_pos = candidate_end

        return text[start_pos:end_pos].strip()

    def _extract_top_block(self, text: str, title: str) -> str:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        title_no_suffix = re.sub(r"\s+Weather Forecast.*$", "", title, flags=re.IGNORECASE).strip()
        title_parts = [p.strip() for p in title_no_suffix.split(",") if p.strip()]

        prefixes = []
        if len(title_parts) >= 2:
            prefixes.append(f"{title_parts[0]}, {title_parts[1]}")
        if title_parts:
            prefixes.append(title_parts[0])

        start_idx = 0
        for i, line in enumerate(lines):
            if any(prefix.lower() in line.lower() for prefix in prefixes):
                start_idx = i
                break

        subset = lines[start_idx:start_idx + 50]
        kept = []
        for line in subset:
            low = line.lower()
            useful = (
                re.match(r"^[A-Za-zÀ-ÿ'’\- ]+,\s*[A-Za-zÀ-ÿ'’\- ]+$", line)
                or re.match(r"^-?\d+°C?$", line)
                or re.match(r"^\d+$", line)
                or re.match(r"^\d{1,3}%$", line)
                or low.startswith("allarme")
                or low.startswith("meteo di ")
                or low.endswith(" weather")
                or low.startswith("realfeel")
                or low.startswith("wind")
                or low.startswith("humidity")
                or low.startswith("uv index")
                or low.startswith("pressure")
                or low.startswith("current weather")
                or low.startswith("meteo attuale")
            )
            if useful:
                kept.append(line)
        return "\n".join(kept).strip()

    def _dedup_all_lines(self, text: str) -> str:
        seen = set()
        result = []
        for line in text.splitlines():
            s = line.strip()
            if not s:
                continue
            key = s.lower()
            if key not in seen:
                seen.add(key)
                result.append(s)
        return "\n".join(result)

    def _clean_lines(self, text: str) -> str:
        lines = [line.strip() for line in text.splitlines() if line.strip()]

        garbage_exact = {"indietro", "back", "usa località attuale", "use current location", "recenti", "recent", "impostazioni", "settings", "guida", "help", "oggi", "today", "orario", "hourly", "mensile", "monthly", "salute e attività", "health & activities", "intorno al mondo", "around the globe", "news", "video", "videos", "chevron left", "chevron right", "visualizza altro", "vedi tutto", "see all", "see more", "nuvole", "clouds", "temperatura", "temperature", "nuvole temperatura", "clouds temperature", "more details", "altri dettagli", "looking ahead", "radar", "minutecast", "daily", "worldwide", "now", "wintercast"}
        garbage_prefixes = ("for business", "warnings", "data suite", "forensics", "advertising", "featured stories", "top stories", "weather news", "products & services", "advertisement", "pubblicità", "dati non supportati", "data not supported", "condizioni di utilizzo", "terms of use", "informativa sulla privacy", "privacy policy", "norme sui cookie", "cookie policy", "fonti dei dati", "data sources", "luoghi vicini", "nearby locations", "accuweather ready", "weather alerts", "winter weather", "location search")

        kept = []
        for line in lines:
            low = line.lower()
            if low in garbage_exact: continue
            if low.startswith(garbage_prefixes): continue
            if line in {"C", "°", "#", "##", "###"}: continue

            if re.match(r"^[A-Za-zÀ-ÿ'’\- ]+,\s*[A-Za-zÀ-ÿ'’\- ]+\s+Weather$", line):
                line = re.sub(r"\s+Weather$", "", line, flags=re.IGNORECASE)
                low = line.lower()
            if low == "current weather":
                line = "CURRENT WEATHER"
                low = line.lower()
            if low == "meteo attuale":
                line = "METEO ATTUALE"
                low = line.lower()
            kept.append(line)

        dedup = []
        prev = None
        for line in kept:
            if line != prev:
                dedup.append(line)
            prev = line
        return "\n".join(dedup).strip()

    def _extract_hurricane_block(self, text: str) -> str:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        kept = []
        for line in lines:
            low = line.lower()
            useful = (
                re.match(r"^\d+$", line)
                or low.startswith("allarme")
                or low.startswith("copia completata")
                or low.startswith("non ci sono tempeste attive")
                or low.startswith("visualizza le tempeste")
                or low.startswith("tempeste passate")
                or low.startswith("category")
                or re.match(r"^[A-Z][A-Z0-9\- ]+$", line)
                or low.startswith("ciclone tropicale")
                or low.startswith(("gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"))
                or low.startswith(("atlantico", "pacifico", "sud pacifico"))
            )
            if useful: kept.append(line)
        dedup = []
        prev = None
        for line in kept:
            if line != prev: dedup.append(line)
            prev = line
        return "\n".join(dedup).strip()

    def _extract_location_weather_block(self, text: str, title: str) -> str:
        top_block = self._extract_top_block(text, title)
        section_specs = [
            ([r"^TONIGHT'?S WEATHER$", r"^Tonight'?s Weather$"], [r"^CURRENT WEATHER$", r"^METEO ATTUALE$"]),
            ([r"^METEO ATTUALE$", r"^CURRENT WEATHER$"], [r"^EVOLUZIONE$", r"^OUTLOOK$", r"^.*RADAR.*$", r"^PREVISIONI ORARIE$", r"^HOURLY WEATHER$"]),
            ([r"^EVOLUZIONE$", r"^OUTLOOK$"], [r"^.*RADAR.*$", r"^PREVISIONI ORARIE$", r"^HOURLY WEATHER$"]),
            ([r"^.*RADAR.*$"], [r"^PREVISIONI ORARIE$", r"^HOURLY WEATHER$", r"^PREVISIONI GIORNO$", r"^DAILY WEATHER$"]),
            ([r"^PREVISIONI ORARIE$", r"^HOURLY WEATHER$"], [r"^PREVISIONI GIORNO$", r"^DAILY WEATHER$", r"^SOLE E LUNA$", r"^SUN & MOON$"]),
            ([r"^PREVISIONI GIORNO$", r"^DAILY WEATHER$"], [r"^SOLE E LUNA$", r"^SUN & MOON$", r"^QUALITÀ DELL'ARIA$", r"^AIR QUALITY$"]),
            ([r"^SOLE E LUNA$", r"^SUN & MOON$"], [r"^QUALITÀ DELL'ARIA$", r"^AIR QUALITY$", r"^SITUAZIONE ALLERGIE$", r"^ALLERGY OUTLOOK$"]),
            ([r"^QUALITÀ DELL'ARIA$", r"^AIR QUALITY$"], [r"^SITUAZIONE ALLERGIE$", r"^ALLERGY OUTLOOK$"]),
            ([r"^SITUAZIONE ALLERGIE$", r"^ALLERGY OUTLOOK$"], []),
        ]

        blocks = []
        if top_block: blocks.append(top_block)

        for start_pats, stop_pats in section_specs:
            section = self._extract_section(text, start_pats, stop_pats)
            if section: blocks.append(section)

        merged = "\n\n".join(blocks)
        merged = self._clean_lines(merged)
        merged = self._dedup_all_lines(merged)
        merged = re.sub(r"\n{3,}", "\n\n", merged)
        return merged.strip()

    def _fallback_generic_weather_text(self, text: str, title: str) -> str:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        kept = []
        for line in lines:
            low = line.lower()
            useful = (
                title.lower() in low
                or re.match(r"^-?\d+°C?$", line)
                or re.match(r"^\d{1,3}%$", line)
                or low.startswith(("realfeel", "humidity", "wind", "pressure", "uv index"))
                or "weather" in low
                or "meteo" in low
                or "air quality" in low
                or "qualità dell'aria" in low
                or "allergy" in low
                or "allerg" in low
                or "sun" in low
                or "moon" in low
                or "sole" in low
                or "luna" in low
            )
            if useful: kept.append(line)

        kept = self._clean_lines("\n".join(kept))
        kept = self._dedup_all_lines(kept)

        if kept.strip(): return kept.strip()

        fallback = []
        for line in lines[:40]:
            low = line.lower()
            if low not in {"today", "oggi", "hourly", "daily", "monthly"}:
                fallback.append(line)

        fallback_text = self._clean_lines("\n".join(fallback))
        fallback_text = self._dedup_all_lines(fallback_text)
        return fallback_text.strip()

    def _parse_accuweather_text(self, text: str, title: str, url: str) -> str:
        if "/hurricane" in url:
            parsed = self._extract_hurricane_block(text)
            if parsed: return parsed
            return self._fallback_generic_weather_text(text, title)

        parsed = self._extract_location_weather_block(text, title)
        if parsed: return parsed
        return self._fallback_generic_weather_text(text, title)