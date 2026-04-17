import re
import asyncio
from pathlib import Path
from urllib.parse import urlparse, unquote

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from parsers.base_parser import BaseParser

class ATPTourParser(BaseParser):
    """Parser per atptour.com basato al 100% su Regex (Niente BeautifulSoup)."""

    def __init__(self) -> None:
        self.browser_config = BrowserConfig(headless=True)
        # Miriamo al corpo dell'articolo per tagliare fuori a monte header e footer
        self.run_config = CrawlerRunConfig(css_selector=".atp_article", magic=True)

    async def parse(self, url: str) -> dict:
        domain = urlparse(url).netloc
        title = self._estrai_titolo_da_url(url)

        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            result = await crawler.arun(url=url, config=self.run_config)

        
        raw_html = result.html or ""
        raw_markdown = result.markdown or ""
        with open("MARKDOWN_SPORCO.txt", "w", encoding="utf-8") as f:
            f.write(raw_markdown)

        parsed_text = self._pulisci_markdown(raw_markdown, title)

        return {
            "url": url,
            "domain": domain,
            "title": title,
            "html_text": raw_html,
            "parsed_text": parsed_text,
        }

    def _estrai_titolo_da_url(self, url: str) -> str:
        """Estrae il titolo dall'URL."""
        slug = urlparse(url).path.split("/")[-1]
        slug = unquote(slug).replace("-", " ")
        return slug.title().strip()

    def _pulisci_markdown(self, md: str, titolo: str) -> str:
        """
        Applica una serie di Regex aggressive per pulire il Markdown
        generato dal sito ATP.
        """
        # Normalizza a capo
        md = re.sub(r"\r\n?", "\n", md)

        # 1. RIMOZIONE RUMORE INIZIALE (Social e intestazioni sporche)
        # Il testo spesso inizia con la lista dei social: * Facebook \n * x \n ecc...
        md = re.sub(r"(?m)^\s*\*\s*(Facebook|x|TikTok|Email)\s*$\n?", "", md, flags=re.IGNORECASE)
        # Rimuove il nome della città isolato all'inizio (es. "Munich")
        md = re.sub(r"(?m)^[A-Z][a-z]+\s*$", "", md) 

        # 2. RIMOZIONE WIDGET VIDEO (Il grosso blocco di configurazione video)
        # Eliminiamo tutto il blocco del player video testuale (da "Video Player is loading." fino a "Close Modal Dialog")
        md = re.sub(r"(?ms)^>\s*.*?—.*?\(\@.*?\).*?\n", "", md)
        md = re.sub(r"(?is)Video Player is loading\..*?Close Modal Dialog", "", md)
        # Rimuovi eventuali righe residue legate al video
        md = re.sub(r"(?mi)^(Play Video|Play|Mute|Current Time.*|Duration.*|Loaded:.*|Stream Type.*|Seek to live.*|Remaining Time.*|Playback Rate|Chapters|Descriptions|Captions|Audio Track|Picture-in-PictureFullscreen|This is a modal window\.|Beginning of dialog window\..*|End of dialog window\.)\s*$", "", md)
        
        # 3. RIMOZIONE BOX CONTENUTI CORRELATI
        md = re.sub(r"(?mi)^You May Also Like:.*$\n?", "", md)

        # 4. RIMOZIONE CODA DELL'ARTICOLO
        # Spesso alla fine ci sono video correlati o altre news. Tagliamo tutto dopo "Top Videos"
        md = re.sub(r"(?ms)^###\s+(Top Videos|View Related Videos|Read More News).*$", "", md)
        
        # Rimuovi l'avviso di Twitter se presente
        md = re.sub(r"(?mi)^X Post\s*$", "", md)

        # 5. PULIZIA LINK (Preserva il testo, toglie l'URL)
        md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)

        # 6. FILTRAGGIO DELLE RIGHE
        linee_pulite = []
        for line in md.splitlines():
            s = line.strip()
            
            if not s:
                continue
                
            # Salta i menu a discesa rimasti
            if s in ["Font Size", "Text Edge Style", "Font Family", "Reset", "Done"]:
                continue

            # Mantiene i titoli (#), e il testo normale
            linee_pulite.append(line)

        md = "\n".join(linee_pulite)

        # 7. FORMATTAZIONE FINALE
        # Assicurati che inizi con il titolo
        if not md.strip().startswith("#"):
             md = f"# {titolo}\n\n{md.strip()}"

        # Elimina spazi orizzontali e verticali eccessivi
        md = re.sub(r"[ \t]{2,}", " ", md)
        md = re.sub(r"\n{3,}", "\n\n", md)

        return md.strip()

