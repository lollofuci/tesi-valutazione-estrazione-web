"""Costruisce l'insieme dei casi di test (results/cases.jsonl).

Per ogni documento del Gold Standard:
- 1 caso "parser": il testo estratto dal parser reale (parsing offline dell'HTML congelato);
- 16 casi "perturbazione": il Gold Standard intatto + 5 tipi x 3 livelli di gravita'.

Uso:  python -m experiments.build_cases [--force-parse]
"""

from __future__ import annotations

import argparse
import json

from evaluation.advanced.perturbations import generate_variants
from evaluation.advanced.text_utils import detect_language
from experiments import config
from experiments.common import load_gold_standard, parse_offline, write_json


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--force-parse", action="store_true", help="rifa il parsing anche se gia' in cache")
    args = ap.parse_args()

    entries = load_gold_standard()
    print(f"Gold Standard: {len(entries)} documenti")
    parsed = parse_offline(entries, force=args.force_parse)

    cases = []
    for e in entries:
        lang = detect_language(e["gold_text"])
        base = {"doc_id": e["doc_id"], "url": e["url"], "domain": e["domain"], "lang": lang}
        cases.append({**base, "case_id": f"{e['doc_id']}|parser", "kind": "parser",
                      "ptype": "parser", "severity": None, "effective_severity": None,
                      "text": parsed[e["url"]]})
        for v in generate_variants(e["gold_text"], e["html_text"], seed=e["url"],
                                   severities=config.SEVERITIES):
            cases.append({**base, "case_id": f"{e['doc_id']}|{v.ptype}|{v.severity}",
                          "kind": "perturbation", "ptype": v.ptype, "severity": v.severity,
                          "effective_severity": v.effective_severity, "text": v.text})

    config.CASES_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(config.CASES_PATH, "w", encoding="utf-8") as f:
        for c in cases:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    write_json(config.RESULTS_DIR / "documents.json",
               [{k: e.get(k, "") for k in ("doc_id", "url", "domain", "title")} for e in entries])
    print(f"Creati {len(cases)} casi in {config.CASES_PATH}")


if __name__ == "__main__":
    main()
