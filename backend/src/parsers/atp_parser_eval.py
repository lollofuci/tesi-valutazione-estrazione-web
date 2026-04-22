from parsers.atptour_parser import ATPTourParser


class ATPTourEvalParser(ATPTourParser):
    """Parser ATP Tour per evaluation sul Gold Standard.

    Usa l'HTML salvato nel GS e lo processa con la stessa logica del parser ATP.
    """

    async def parse(self, url: str, html_text: str) -> dict:
        return await self.parse_from_html(url, html_text)