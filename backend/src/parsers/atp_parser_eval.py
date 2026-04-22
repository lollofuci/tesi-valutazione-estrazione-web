import re
import html as html_lib
from urllib.parse import urlparse

from parsers.atptour_parser import ATPTourParser


class ATPTourEvalParser(ATPTourParser):
    """Parser ATP Tour per evaluation sul Gold Standard.

    Non rilancia Crawl4AI su html salvato.
    Estrae testo semplice dal GS e poi applica la stessa logica finale
    del parser ATP live.
    """

    async def parse_from_html(self, url: str, html: str) -> dict:
        domain = urlparse(url).netloc
        title = self._estrai_titolo_da_url(url)

        text = self._html_to_text_for_eval(html)
        parsed_text = self._smista_e_pulisci(url, text, title)

        return {
            "url": url,
            "domain": domain,
            "title": title,
            "html_text": html,
            "parsed_text": parsed_text,
        }

    def _html_to_text_for_eval(self, html: str) -> str:
        text = html

        # Rimuovi script/style
        text = re.sub(
            r"<script\b[^>]*>.*?</script>",
            "",
            text,
            flags=re.IGNORECASE | re.DOTALL,
        )
        text = re.sub(
            r"<style\b[^>]*>.*?</style>",
            "",
            text,
            flags=re.IGNORECASE | re.DOTALL,
        )

        # Heading -> markdown leggero
        text = re.sub(r"<h1\b[^>]*>", "\n# ", text, flags=re.IGNORECASE)
        text = re.sub(r"<h2\b[^>]*>", "\n## ", text, flags=re.IGNORECASE)
        text = re.sub(r"<h3\b[^>]*>", "\n### ", text, flags=re.IGNORECASE)
        text = re.sub(r"</h[1-6]>", "\n", text, flags=re.IGNORECASE)

        # Tag di blocco -> newline
        text = re.sub(r"</?(br|hr)\b[^>]*>", "\n", text, flags=re.IGNORECASE)
        text = re.sub(
            r"</?(p|div|section|article|main|aside|header|footer|li|ul|ol|span|table|tr|td|th)\b[^>]*>",
            "\n",
            text,
            flags=re.IGNORECASE,
        )

        # Rimuovi gli altri tag
        text = re.sub(r"<[^>]+>", " ", text)

        # Decode entità HTML
        text = html_lib.unescape(text)

        # Normalizzazione
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n[ \t]+", "\n", text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Rimuovi righe vuote e schifezze evidenti
        lines = []
        for raw_line in text.splitlines():
            line = raw_line.strip()
            if not line:
                continue

            low = line.lower()

            garbage_prefixes = (
                "cookie",
                "privacy",
                "terms",
                "accept",
                "search",
                "shop",
                "buy tickets",
                "more navigation links",
                "header 2",
            )
            if low.startswith(garbage_prefixes):
                continue

            lines.append(line)

        return "\n".join(lines).strip()