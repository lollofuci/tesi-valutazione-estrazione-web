from urllib.parse import urlparse
import asyncio

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


def clean_wikipedia_markdown(text: str) -> str:
    skip_titles = {
        "## note",
        "## bibliografia",
        "## altri progetti",
        "## collegamenti esterni",
        "## voci correlate"
    }

    lines = text.splitlines()
    cleaned_lines = []

    for line in lines:
        stripped = line.strip()

        if not stripped:
            continue

        if stripped.lower() in skip_titles:
            break

        cleaned_lines.append(stripped)

    return "\n\n".join(cleaned_lines).strip()


class WikipediaParser:
    async def _parse_async(self, url: str) -> dict:
        domain = urlparse(url).netloc.lower()

        browser_config = BrowserConfig(
            headless=True
        )

        run_config = CrawlerRunConfig(
            word_count_threshold=1,
            remove_overlay_elements=True,
            process_iframes=False,
            exclude_external_links=True,
            exclude_social_media_links=True,
            markdown_generator=DefaultMarkdownGenerator(),
            verbose=False
        )

        async with AsyncWebCrawler(config=browser_config) as crawler:
            result = await crawler.arun(url=url, config=run_config)

        if not result.success:
            raise ValueError(f"Errore nel parsing di {url}: {result.error_message}")

        html_text = result.html or ""
        title = result.metadata.get("title", "") if result.metadata else ""

        parsed_text = ""
        markdown_result = getattr(result, "markdown", None)

        if markdown_result:
            if isinstance(markdown_result, str):
                parsed_text = markdown_result.strip()
            elif hasattr(markdown_result, "fit_markdown") and markdown_result.fit_markdown:
                parsed_text = markdown_result.fit_markdown.strip()
            elif hasattr(markdown_result, "raw_markdown") and markdown_result.raw_markdown:
                parsed_text = markdown_result.raw_markdown.strip()
            else:
                parsed_text = str(markdown_result).strip()

        parsed_text = clean_wikipedia_markdown(parsed_text)

        return {
            "url": url,
            "domain": domain,
            "title": title,
            "html_text": html_text,
            "parsed_text": parsed_text
        }

    def parse(self, url: str) -> dict:
        return asyncio.run(self._parse_async(url))