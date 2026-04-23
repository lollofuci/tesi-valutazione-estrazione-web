import asyncio
import json

from parsers.wikipedia_parser import WikipediaParser
from parsers.tradingeconomics_parser import TradingEconomicsParser
from parsers.atptour_parser import ATPTourParser
from evaluation.evaluator import token_level_eval, aggregate_metrics


async def main():
    with open("../../gs_data/atptour_gs.json", "r", encoding="utf-8") as f:
        gs_data = json.load(f)

    parser = ATPTourParser()
    metrics_list = []

    for entry in gs_data:
        url = entry["url"]
        gold_text = entry["gold_text"]
        html_text = entry["html_text"]
        try:
            parsed_result = await parser.parse(url)
            print(f"parsed_text: '{parsed_result['parsed_text'][:200]}'")
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