import asyncio
import json

from parsers.new_wikipedia_parser import WikipediaParser
from evaluation.evaluator import token_level_eval, aggregate_metrics


async def main():
    with open("../../gs_data/wikipedia_gs.json", "r", encoding="utf-8") as f:
        gs_data = json.load(f)

    parser = WikipediaParser()
    metrics_list = []

    for entry in gs_data:
        url = entry["url"]
        gold_text = entry["gold_text"]

        try:
            parsed_result = await parser.parse(url)
            metrics = token_level_eval(
                parsed_text=parsed_result["parsed_text"],
                gold_text=gold_text,
            )
            metrics_list.append(metrics)

            print(f"\nURL: {url}")
            print(metrics)

        except Exception as e:
            print(f"\nErrore su {url}: {e}")

    final_metrics = aggregate_metrics(metrics_list)

    print("\n=== METRICHE FINALI ===")
    print(final_metrics)


if __name__ == "__main__":
    asyncio.run(main())