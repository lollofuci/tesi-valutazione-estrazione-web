import asyncio
import json

from parsers.accuweather_parser import AccuWeatherParser
from parsers.wikipedia_parser import WikipediaParser
from evaluation.evaluator import token_level_eval


async def main():
    url = "https://www.accuweather.com/it/it/rome/213490/weather-forecast/213490"

    # carica il GS
    with open("../../gs_data/accuweather.json", "r", encoding="utf-8") as f:
        gs_data = json.load(f)

    # cerca l'entry del GS con quell'url
    gold_entry = None
    for entry in gs_data:
        if entry["url"] == url:
            gold_entry = entry
            break

    if gold_entry is None:
        raise ValueError(f"URL {url} non trovato nel gold standard")

    parser = AccuWeatherParser()
    parsed_result = await parser.parse(url)

    metrics = token_level_eval(
        parsed_text=parsed_result["parsed_text"],
        gold_text=gold_entry["gold_text"],
    )

    print("TITLE:", parsed_result["title"])
    print("METRICS:", metrics)


if __name__ == "__main__":
    asyncio.run(main())