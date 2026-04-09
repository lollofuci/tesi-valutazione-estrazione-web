from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from urllib.parse import urlparse


class WikipediaParser:
    async def parse(self, url: str) -> dict:
        """
        Parser per pagine Wikipedia.
        Restituisce un dizionario con:
        url, domain, title, html_text, parsed_text
        """

        domain = urlparse(url).netloc

        # Configurazione base del crawler (dalle slide)
        browser_config = BrowserConfig(headless=True)

        run_config = CrawlerRunConfig(
            # puoi modificare questi parametri più avanti
        )

        async with AsyncWebCrawler(config=browser_config) as crawler:
            result = await crawler.arun(url=url, config=run_config)

        # ⚠️ questi campi dipendono da Crawl4AI
        html_text = result.html if hasattr(result, "html") else ""
        markdown = result.markdown if hasattr(result, "markdown") else ""

        # titolo (semplificato per ora)
        title = result.title if hasattr(result, "title") else ""

        # parsed_text = markdown pulito
        parsed_text = self.clean_text(markdown)

        return {
            "url": url,
            "domain": domain,
            "title": title,
            "html_text": html_text,
            "parsed_text": parsed_text,
        }

    def clean_text(self, text: str) -> str:
        """
        Pulizia base del testo markdown.
        """
        lines = text.split("\n")
        cleaned_lines = [line.strip() for line in lines if line.strip() != ""]
        return "\n".join(cleaned_lines)