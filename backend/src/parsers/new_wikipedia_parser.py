import re
from urllib.parse import urlparse, unquote

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

from parsers.base_parser import BaseParser


class WikipediaParser(BaseParser):

    def __init__(self) -> None:
        self.browser_config = BrowserConfig(headless=True)
        # Selezioniamo il corpo centrale del testo, ignorando elementi di navigazione
        self.run_config = CrawlerRunConfig(css_selector="#bodyContent")

    async def parse(self, url: str) -> dict:
        domain = urlparse(url).netloc
        title = self._estrai_titolo_da_url(url)

        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            result = await crawler.arun(url=url, config=self.run_config)

        if not result.success:
            error_message = getattr(result, "error_message", "Errore sconosciuto")
            raise RuntimeError(f"Crawl fallito: {error_message}")

        parsed_text = self._pulisci_markdown(result.markdown, url)

        return {
            "url": url,
            "domain": domain,
            "title": title,
            "html_text": result.html,
            "parsed_text": parsed_text,
        }

    def _estrai_titolo_da_url(self, url: str) -> str:
        slug = urlparse(url).path.split("/wiki/")[-1]
        # Puliamo il titolo da eventuali parentesi per il matching esatto
        slug = re.sub(r"_\(.*?\)", "", slug) 
        return unquote(slug).replace("_", " ").strip()

    def _pulisci_markdown(self, md: str, url: str) -> str:
        titolo = self._estrai_titolo_da_url(url)
        
        # 1. TAGLIO DI TESTA (Anti-Infobox)
        match_def = re.search(rf"(?mi)\*\*{re.escape(titolo)}.*?\*\*", md)
        if match_def:
            inizio = md.rfind("\n", 0, match_def.start())
            md = md[inizio if inizio != -1 else match_def.start():]
        else:
            match_generic = re.search(r"(?mi)^\s*\*\*.*?\*\*\s*\(", md)
            if match_generic:
                md = md[match_generic.start():]

        # 2. TAGLIO DI CODA (Anti-Navbox e Bibliografia)
        md = re.sub(r"(?ms)^##\s+(Note|Bibliografia|Voci correlate|Altri progetti|Collegamenti esterni|Categorie|Note e progetti|Fonti).*", "", md)

        # 3. RIMOZIONE RUMORE INLINE E PULIZIA MARKDOWN
        sostituzioni = [
            # KILLER DEI LINK
            (r"\[\[(.*?)\]\]\((?:[^)(]+|\([^)(]*\))*\)", r"\1"), (r"\[(.*?)\]\((?:[^)(]+|\([^)(]*\))*\)", r"\1"),  
            
            # KILLER DEGLI AVVISI WIKIPEDIA
            (r"(?i)Questa voce o sezione.*?\.", ""), (r"(?i)Commento\s*:.*", ""),
            
            # KILLER DELLA PRONUNCIA E MULTIMEDIA
            (r"\s*\([^)]*AFI:[^)]*\)", ""), (r"ascoltaⓘ", ""), (r"pronunciaⓘ", ""), (r"(?i)!\[.*?\]\(.*?\)", ""), (r"(?im)^.*?\.(jpg|jpeg|png|svg|webp|pdf|gif).*?$", ""),
            
            # PULIZIA RESIDUI WIKIPEDIA
            (r"\[modifica\s*\|\s*modifica wikitesto\]", ""),
            (r"\[\s*nota\s*\d+(?:\s*,\s*\d+)*\s*\]", ""),
            (r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]", ""),
            (r"Coordinate:.*", ""),
            (r"Da Wikipedia, l'enciclopedia libera\.", ""),
            (r"Lo stesso argomento in dettaglio:.*", ""),          
            
            # PULIZIA SINTASSI MARKDOWN (Non rimuoviamo '|' perché serve alle tabelle)
            (r"\*\*", ""), (r"_", ""), (r"\\\(", "("), (r"\\\)", ")"), (r"(?m)^\s*\*\s*\*\s*\*\s*$", ""), 
        ]
        
        for pattern, repl in sostituzioni:
            md = re.sub(pattern, repl, md, flags=re.IGNORECASE)


        #ULTIMA PARTE CAMBIATA -> SE RISCONTRI PROBLEMI CON I TEST FOCALIZZATI QUI ---------------------------------------------------------


            # Rimuove numeri-nota attaccati alle parole: Roma6 -> Roma, abitanti2 -> abitanti
            md = re.sub(r"(?<=[A-Za-zÀ-ÖØ-öø-ÿ])\d+\b", "", md)

            # Rimuove numeri-nota prima della punteggiatura: Stato.7 -> Stato.
            md = re.sub(r"\b\d+(?=[,.;:!?])", "", md)

        # 4. FILTRAGGIO RIGHE E PRESERVAZIONE TABELLE
        linee_pulite = []
        for line in md.splitlines():
            s = line.strip()
            
            if not s:
                continue

            # PRESERVIAMO LE TABELLE (Righe che iniziano con | o contengono la struttura delle tabelle MD)
            if s.startswith('|') or s.startswith('+-') or (s.count('|') > 1):
                linee_pulite.append(line)
                continue

            # Preserviamo liste e titoli
            if s.startswith(('*', '-', '1.', '#')):
                linee_pulite.append(line)
                continue

            # Filtro per frasi troppo corte (solo se non sono tabelle/liste)
            # Aiuta a eliminare didascalie o frammenti isolati
            if len(s) < 30 and not re.search(r"\b(è|sono|fu|era|si trova|ospita|rappresenta|nato|morto)\b", s, re.I):
                if not s.endswith((".", ":", ";")):
                    continue
            
            linee_pulite.append(line)

        # 5. NORMALIZZAZIONE SPAZI
        md = "\n".join(linee_pulite)
        # Riduciamo gli spazi multipli ma facciamo attenzione a non rompere l'allineamento tabelle
        md = re.sub(r"[ \t]{2,}", " ", md) 
        md = re.sub(r"\n{3,}", "\n\n", md)

        return md.strip()