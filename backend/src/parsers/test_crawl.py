import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig


async def main():
    browser_config = BrowserConfig(headless=True)
    run_config = CrawlerRunConfig()

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://it.wikipedia.org/wiki/Avellino",
            config=run_config
        )

    print("SUCCESS:", result.success)
    print("HTML:")
    print(result.html[:500])

    print("\nMARKDOWN:")
    markdown = getattr(result, "markdown", "")
    print(str(markdown)[:500])


if __name__ == "__main__":
    asyncio.run(main())