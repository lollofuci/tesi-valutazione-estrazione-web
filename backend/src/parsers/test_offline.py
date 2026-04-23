import asyncio
import json
from pathlib import Path

from parsers.accuweather_parser import AccuWeatherParser

async def main():
    # 1. Trova e carica il tuo file Gold Standard
    # Assicurati che il nome del file sia corretto (es. accuweather.json o accuweather_gs.json)
    gs_path = Path("gs_data/accuweather.json") 
    
    try:
        with open(gs_path, "r", encoding="utf-8") as f:
            gs_data = json.load(f)
    except FileNotFoundError:
        print(f"ERRORE: File {gs_path} non trovato!")
        return

    # Scegli l'URL esatto che vuoi controllare (DEVE essere uno di quelli nel JSON)
    target_url = "https://www.accuweather.com/it/it/rome/213490/weather-forecast/213490"

    # 2. Cerca i dati salvati per quell'URL
    gs_entry = None
    for item in gs_data:
        if item["url"] == target_url:
            gs_entry = item
            break

    if not gs_entry:
        print(f"ERRORE: L'URL {target_url} non è presente nel Gold Standard.")
        return

    print("Inizio parsing OFFLINE dal file JSON...")
    
    # 3. Inizializza il parser ed esegui parse_from_html
    parser = AccuWeatherParser()
    result = await parser.parse_from_html(gs_entry["url"], gs_entry["html_text"])

    parsed_text = result["parsed_text"]
    gold_text = gs_entry["gold_text"]

    # 4. Stampa i due testi vicini per trovare il colpevole!
    print("\n" + "="*60)
    print("🥇 GOLD STANDARD (Quello che si aspetta il test):")
    print("="*60)
    print(gold_text)

    print("\n" + "="*60)
    print("🤖 PARSED TEXT (Quello che il tuo codice estrae ora):")
    print("="*60)
    print(parsed_text)

    print("\n" + "="*60)
    print(f"📊 LUNGHEZZA GOLD: {len(gold_text)} caratteri")
    print(f"📊 LUNGHEZZA PARSED: {len(parsed_text)} caratteri")
    print("="*60)
    print("💡 SUGGERIMENTO: Fai copia-incolla dei due blocchi di testo su un sito come 'diffchecker.com' per vedere le differenze evidenziate in rosso/verde!")

if __name__ == "__main__":
    asyncio.run(main())