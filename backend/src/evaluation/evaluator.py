import re
import mistune
from bs4 import BeautifulSoup


def remove_markdown(md: str) -> str:
    if not md:
        return ""

    html = mistune.html(md)
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup.find_all(True):
        tag.unwrap()

    text = re.sub(r"[ \t]+", " ", str(soup))
    text = re.sub(r"\n+", "\n", text)

    return text.strip()


def tokenized_text(text: str) -> set[str]:
    normalized = re.sub(r"\s+", " ", text.lower()).strip()
    if not normalized:
        return set()
    return set(normalized.split())


def token_level_eval(parsed_text: str, gold_text: str) -> dict[str, float]:
    parsed_plain = remove_markdown(parsed_text)
    gold_plain = remove_markdown(gold_text)

    parsed_tokens = tokenized_text(parsed_plain)
    gold_tokens = tokenized_text(gold_plain)

    intersection = parsed_tokens & gold_tokens

    precision = len(intersection) / len(parsed_tokens) if parsed_tokens else 0.0
    recall = len(intersection) / len(gold_tokens) if gold_tokens else 0.0

    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall) > 0
        else 0.0
    )

    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


def aggregate_metrics(metrics_list: list[dict[str, float]]) -> dict[str, float]:
    if not metrics_list:
        return {
            "precision": 0.0,
            "recall": 0.0,
            "f1": 0.0,
        }

    n = len(metrics_list)

    return {
        "precision": sum(m["precision"] for m in metrics_list) / n,
        "recall": sum(m["recall"] for m in metrics_list) / n,
        "f1": sum(m["f1"] for m in metrics_list) / n,
    }