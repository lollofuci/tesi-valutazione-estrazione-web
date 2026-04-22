from abc import ABC, abstractmethod
import re


class BaseParser(ABC):
    """Classe astratta base per tutti i parser."""

    @abstractmethod
    async def parse(self, url: str) -> dict:
        """Dato un URL, scarica la pagina e restituisce i dati parsati."""
        raise NotImplementedError

    @abstractmethod
    async def parse_from_html(self, url: str, html: str) -> dict:
        """Dato un URL e l'HTML grezzo, restituisce i dati parsati."""
        raise NotImplementedError

    def clean_markdown(self, md: str) -> str:
        """
        Ripulisce un testo Markdown preservandone la struttura.
        Non converte in plain text: mantiene titoli, liste e paragrafi.
        """
        if not md:
            return ""

        md = md.replace("\r\n", "\n").replace("\r", "\n")
        md = re.sub(r"[ \t]+\n", "\n", md)
        md = re.sub(r"\n{3,}", "\n\n", md)

        return md.strip()