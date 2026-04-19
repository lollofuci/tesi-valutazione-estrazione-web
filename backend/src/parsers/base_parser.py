from abc import ABC, abstractmethod


class BaseParser(ABC):
    """Classe astratta base per tutti i parser."""

    @abstractmethod
    async def parse(self, url: str) -> dict:
        """Dato un URL, restituisce i dati parsati."""
        raise NotImplementedError

    @abstractmethod
    async def parse_from_html(self, url: str, html: str) -> dict:
        """Dato un URL e l'HTML grezzo, restituisce i dati parsati."""
        raise NotImplementedError