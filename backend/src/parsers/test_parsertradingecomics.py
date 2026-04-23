import asyncio
import sys
sys.path.append("..")

from parsers.tradingeconomics_parser import TradingEconomicsParser

async def main():
    parser = TradingEconomicsParser()
    risultato = await parser.parse("https://tradingeconomics.com/euro-area/gdp")
    
    print(f"Titolo: {risultato['title']}")
    print(f"Parsed text ({len(risultato['parsed_text'])} caratteri):\n")
    print(risultato["parsed_text"])

    with open("output_parsed.txt", "w") as f:
        f.write(f"TITOLO: {risultato['title']}\n\n")
        f.write(risultato["parsed_text"])
    with open("output_html.txt", "w") as f:          # ← assicurati ci sia anche questo
        f.write(risultato["html_text"])
    print("Salvato!")

asyncio.run(main())