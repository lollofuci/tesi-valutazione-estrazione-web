"""Calcola tutte le metriche su tutti i casi (results/metrics.jsonl).

Lo script e' riprendibile: i casi gia' presenti in metrics.jsonl vengono saltati, quindi
se viene interrotto basta rilanciarlo.

Se un caso era stato calcolato senza BERTScore e ora BERTScore e' richiesto, viene
ricalcolato (nell'analisi vale l'ultima riga di ogni caso).

Uso:  python -m experiments.run_metrics [--no-bertscore]
"""

from __future__ import annotations

import argparse
import time

from evaluation.advanced.metrics import lexical_metrics
from experiments import config
from experiments.common import append_jsonl, fmt_seconds, gold_by_url, load_cases, read_jsonl


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--no-bertscore", action="store_true", help="salta BERTScore (piu' lento)")
    args = ap.parse_args()

    cases = load_cases()
    gold = gold_by_url()
    rows = read_jsonl(config.METRICS_PATH)
    if args.no_bertscore:
        done = {row["case_id"] for row in rows}
    else:
        done = {row["case_id"] for row in rows if "bertscore_f" in row}
    todo = [c for c in cases if c["case_id"] not in done]
    print(f"Casi: {len(cases)} totali, {len(done)} gia' calcolati, {len(todo)} da calcolare")

    scorer = None
    if not args.no_bertscore:
        from evaluation.advanced.bertscore import LongBertScorer
        scorer = LongBertScorer()
        print(f"BERTScore: modello {scorer.model_name}, strato {scorer.layer}")

    # ordinati per documento: il Gold Standard di ciascun documento viene codificato una volta sola
    todo.sort(key=lambda c: c["doc_id"])
    start = time.perf_counter()
    current_doc = None
    for i, case in enumerate(todo, start=1):
        if scorer is not None and case["doc_id"] != current_doc:
            scorer.clear_cache()
            current_doc = case["doc_id"]
        reference = gold[case["url"]]
        t0 = time.perf_counter()
        row = {"case_id": case["case_id"]}
        row.update(lexical_metrics(case["text"], reference, lang=case["lang"]))
        if scorer is not None:
            for key, value in scorer.score(case["text"], reference).items():
                row[f"bertscore_{key}"] = value
        row["seconds"] = round(time.perf_counter() - t0, 3)
        append_jsonl(config.METRICS_PATH, row)

        elapsed = time.perf_counter() - start
        eta = elapsed / i * (len(todo) - i)
        print(f"[{i}/{len(todo)}] {case['case_id']:<40} token_f={row['token_f']:.3f} "
              f"rougeL_f={row['rougeL_f']:.3f} ({row['seconds']:.1f}s, fine tra ~{fmt_seconds(eta)})")

    print(f"Fatto. Risultati in {config.METRICS_PATH}")


if __name__ == "__main__":
    main()
