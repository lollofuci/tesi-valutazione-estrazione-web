from abc import ABC, abstractmethod
from models import ParsedDocument


class BaseParser(ABC):
    @abstractmethod
    async def parse(self, url: str) -> ParsedDocument:
        """Parsa una pagina web e restituisce un documento strutturato."""