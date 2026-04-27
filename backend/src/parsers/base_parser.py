from abc import ABC, abstractmethod
import re


class BaseParser(ABC):
   
    @abstractmethod
    async def parse(self, url: str) -> dict:
        raise NotImplementedError

    @abstractmethod
    async def parse_from_html(self, url: str, html: str) -> dict:
        raise NotImplementedError

    def clean_markdown(self, md: str) -> str:
        if not md:
            return ""

        md = md.replace("\r\n", "\n").replace("\r", "\n")
        md = re.sub(r"[ \t]+\n", "\n", md)
        md = re.sub(r"\n{3,}", "\n\n", md)

        return md.strip()