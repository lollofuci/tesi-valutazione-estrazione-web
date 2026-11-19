"""Lettura del Gold Standard, parsing offline e gestione dei file di risultati."""

from __future__ import annotations

import asyncio
import json
import re
from pathlib import Path
from urllib.parse import urlparse

from experiments import config


# ---------------------------------------------------------------------------
# Gold Standard e parser
# ---------------------------------------------------------------------------

def load_gold_standard() -> list[dict]:
    """Tutte le voci dei file gs_data/*.json, con un identificativo breve (doc_id)."""
    entries = []
    for path in sorted(config.GS_DIR.glob("*_gs.json")):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        for i, entry in enumerate(data, start=1):
            prefix = path.stem.replace("_gs", "")
            entry = dict(entry)
            entry["domain"] = entry.get("domain") or urlparse(entry["url"]).netloc
            entry["doc_id"] = f"{prefix}-{i:02d}"
            entries.append(entry)
    return entries


def get_parser(domain: str):
    """Stessa associazione dominio -> parser del server (import ritardati)."""
    domain = domain.lower()
    if domain == "it.wikipedia.org":
        from parsers.wikipedia_parser import WikipediaParser
        return WikipediaParser()
    if domain == "www.atptour.com":
        from parsers.atptour_parser import ATPTourParser
        return ATPTourParser()
    if domain == "www.accuweather.com":
        from parsers.accuweather_parser import AccuWeatherParser
        return AccuWeatherParser()
    if domain == "tradingeconomics.com":
        from parsers.tradingeconomics_parser import TradingEconomicsParser
        return TradingEconomicsParser()
    raise ValueError(f"Dominio non supportato: {domain}")


async def _parse_offline(entries: list[dict]) -> dict[str, str]:
    parsed = {}
    for entry in entries:
        parser = get_parser(entry["domain"])
        result = await parser.parse_from_html(entry["url"], entry["html_text"])
        parsed[entry["url"]] = result.get("parsed_text", "")
        print(f"  parsing offline: {entry['doc_id']}  ({len(parsed[entry['url']])} caratteri)")
    return parsed


def parse_offline(entries: list[dict], force: bool = False) -> dict[str, str]:
    """Output dei parser sull'HTML congelato del GS (memorizzato in parsed_outputs.json)."""
    if config.PARSED_PATH.exists() and not force:
        with open(config.PARSED_PATH, encoding="utf-8") as f:
            cached = json.load(f)
        if all(e["url"] in cached for e in entries):
            return cached
    parsed = asyncio.run(_parse_offline(entries))
    write_json(config.PARSED_PATH, parsed)
    return parsed


# ---------------------------------------------------------------------------
# File di risultati (JSON Lines: una riga per caso, scrittura incrementale)
# ---------------------------------------------------------------------------

def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def load_cases() -> list[dict]:
    cases = read_jsonl(config.CASES_PATH)
    if not cases:
        raise SystemExit("Nessun caso trovato: eseguire prima `python -m experiments.build_cases`.")
    return cases


def html_by_url() -> dict[str, str]:
    return {e["url"]: e["html_text"] for e in load_gold_standard()}


def gold_by_url() -> dict[str, str]:
    return {e["url"]: e["gold_text"] for e in load_gold_standard()}


def fmt_seconds(seconds: float) -> str:
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h}h{m:02d}m" if h else f"{m}m{s:02d}s"


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
