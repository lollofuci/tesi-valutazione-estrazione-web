
import sys
import os
import asyncio
sys.path.append(os.path.join(os.path.dirname(__file__), "../backend/src"))

from parsers.tradingeconomics_parser import TradingEconomicsParser
import json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(BASE_DIR, "html")



from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
async def salva_html():
    config = BrowserConfig(headless=True)
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        page_timeout=90000,
        delay_before_return_html=12.0,
        wait_until="networkidle"
    )
    
    urls = {
        "https://tradingeconomics.com/italy/gdp": os.path.join(HTML_DIR, "italy_gdp.html"),
        "https://tradingeconomics.com/commodity/crude-oil": os.path.join(HTML_DIR, "crude_oil.html"),
        "https://tradingeconomics.com/crypto": os.path.join(HTML_DIR, "crypto.html"),
        "https://tradingeconomics.com/germany/gdp": os.path.join(HTML_DIR, "germany_gdp.html"),
        "https://tradingeconomics.com/country-list/gdp-growth-rate": os.path.join(HTML_DIR, "growth_rate.html"),
    }
    
    os.makedirs(HTML_DIR, exist_ok=True)
    print(f"Salvo in: {HTML_DIR}")
    
    async with AsyncWebCrawler(config=config) as crawler:
        for url, filepath in urls.items():
            print(f"Scarico {url}...")
            result = await crawler.arun(url=url, config=run_config)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(result.html)
            print(f"✓ Salvato {filepath}")
asyncio.run(salva_html())