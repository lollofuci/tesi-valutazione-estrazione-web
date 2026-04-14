import asyncio
import json

from parsers.wikipedia_parser import WikipediaParser
from evaluation.evaluator import token_level_eval


async def main():
    url = "https://it.wikipedia.org/wiki/Avellino"

    # carica il GS
    with open("../../gs_data/wikipedia_gs.json", "r", encoding="utf-8") as f:
        gs_data = json.load(f)

    # cerca l'entry del GS con quell'url
    gold_entry = None
    for entry in gs_data:
        if entry["url"] == url:
            gold_entry = entry
            break

    if gold_entry is None:
        raise ValueError(f"URL {url} non trovato nel gold standard")

    parser = WikipediaParser()
    parsed_result = await parser.parse(url)

    metrics = token_level_eval(
        parsed_text=parsed_result["parsed_text"],
        gold_text=gold_entry["gold_text"],
    )

    print("TITLE:", parsed_result["title"])
    print("METRICS:", metrics)


if __name__ == "__main__":
    asyncio.run(main())