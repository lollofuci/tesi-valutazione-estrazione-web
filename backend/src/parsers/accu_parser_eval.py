import re

from parsers.accuweather_parser import AccuWeatherParser


class AccuWeatherEvalParser(AccuWeatherParser):
    """Parser AccuWeather per evaluation sul Gold Standard.

    Usa l'HTML del GS senza richiamare Crawl4AI, ma riutilizza la stessa
    pipeline finale del parser live (_extract_title, _clean_markdown,
    _build_result).
    """

    async def parse(self, url: str, html_text: str) -> dict:
        markdown = self._html_to_markdown_for_eval(html_text)
        return self._build_result(url, html_text, markdown)

    def _html_to_markdown_for_eval(self, html: str) -> str:
        text = html

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

        text = re.sub(r"</?(br|hr)\b[^>]*>", "\n", text, flags=re.IGNORECASE)
        text = re.sub(
            r"</?(p|div|section|article|main|aside|header|footer|li|ul|ol)\b[^>]*>",
            "\n",
            text,
            flags=re.IGNORECASE,
        )

        text = re.sub(r"<h1\b[^>]*>", "\n# ", text, flags=re.IGNORECASE)
        text = re.sub(r"<h2\b[^>]*>", "\n## ", text, flags=re.IGNORECASE)
        text = re.sub(r"<h3\b[^>]*>", "\n### ", text, flags=re.IGNORECASE)
        text = re.sub(r"</h[1-6]>", "\n", text, flags=re.IGNORECASE)

        text = re.sub(r"<[^>]+>", " ", text)

        text = text.replace("&nbsp;", " ")
        text = text.replace("&amp;", "&")
        text = text.replace("&lt;", "<")
        text = text.replace("&gt;", ">")
        text = text.replace("&quot;", '"')
        text = text.replace("&#39;", "'")

        text = text.replace("\r\n", "\n").replace("\r", "\n")
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n[ \t]+", "\n", text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text