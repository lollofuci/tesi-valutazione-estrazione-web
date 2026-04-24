import sys
import os
import asyncio
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(BASE_DIR, "html")

sys.path.append(os.path.join(BASE_DIR, "../backend/src"))
from parsers.tradingeconomics_parser import TradingEconomicsParser

async def make_gs():
    parser = TradingEconomicsParser()
    
    entries = [
        ("https://tradingeconomics.com/italy/gdp", os.path.join(HTML_DIR, "italy_gdp.html"), "Italy GDP"),
        ("https://tradingeconomics.com/commodity/crude-oil", os.path.join(HTML_DIR, "crude_oil.html"), "Crude Oil"),
        ("https://tradingeconomics.com/crypto", os.path.join(HTML_DIR, "crypto.html"), "Crypto"),
        ("https://tradingeconomics.com/germany/gdp", os.path.join(HTML_DIR, "germany_gdp.html"), "Germany GDP"),
        ("https://tradingeconomics.com/country-list/gdp-growth-rate", os.path.join(HTML_DIR, "growth_rate.html"), "GDP Growth Rate by Country"),
    ]
    
    gs = []
    for url, html_file, title in entries:
        print(f"Processing {url}...")
        with open(html_file, "r", encoding="utf-8") as f:
            html_text = f.read()
        
        result = await parser.parse_from_html(url, html_text)
        gold_text = result["parsed_text"]
        
        gs.append({
            "url": url,
            "domain": "tradingeconomics.com",
            "title": title,
            "html_text": html_text,
            "gold_text": gold_text
        })
        print(f"✓ {url}")
    
    output_path = os.path.join(BASE_DIR, "tradingeconomics_gs.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(gs, f, ensure_ascii=False, indent=2)
    
    print(f"Gold standard salvato in {output_path}")

asyncio.run(make_gs())