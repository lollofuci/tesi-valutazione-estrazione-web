import asyncio
import json

# Assicurati che l'import punti al file corretto dove hai il tuo WikipediaParser
from parsers.new_wikipedia_parser import WikipediaParser

async def main():
    url_avellino = "https://it.wikipedia.org/wiki/Avellino"
    
    print(f"🔄 Avvio il parsing per: {url_avellino}...")
    parser = WikipediaParser()
    
    try:
        # 1. Estrazione tramite il tuo parser
        risultato = await parser.parse(url_avellino)
        testo_estratto = risultato["parsed_text"]
        
        # 2. Salvataggio dell'output del parser su file
        with open("avellino_parsed.txt", "w", encoding="utf-8") as f_out:
            f_out.write(testo_estratto)
        print("✅ File 'avellino_parsed.txt' generato con successo!")

        # 3. Estrazione del Gold Standard corrispondente (per confronto)
        # Assicurati che il percorso del file JSON sia corretto
        try:
            with open("../../gs_data/wikipedia_gs.json", "r", encoding="utf-8") as f_gs:
                gs_data = json.load(f_gs)
                for entry in gs_data:
                    if entry["url"] == url_avellino:
                        with open("avellino_gold.txt", "w", encoding="utf-8") as f_gold:
                            f_gold.write(entry["gold_text"])
                        print("✅ File 'avellino_gold.txt' generato con successo!")
                        break
        except FileNotFoundError:
            print("⚠️ File del Gold Standard non trovato, ma ho salvato l'output del parser.")

    except Exception as e:
        print(f"❌ Errore durante il parsing: {e}")

if __name__ == "__main__":
    asyncio.run(main())