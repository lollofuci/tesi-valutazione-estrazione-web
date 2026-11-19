"""Fa valutare i casi ai giudici LLM (results/judges.jsonl).

Casi giudicati (per non impiegare giorni su un portatile):
- gli output reali dei parser (20);
- il Gold Standard intatto (20);
- ogni tipo di perturbazione alla severity JUDGE_SEVERITY (20 x 5).
Con --all si giudicano invece tutti i casi.

Lo script e' riprendibile: le coppie (caso, modello, modalita') gia' presenti vengono
saltate. Si puo' interrompere con Ctrl+C e rilanciare quando si vuole.

Esempi:
    python -m experiments.run_judges --models llama3.2:1b qwen3:4b
    python -m experiments.run_judges --modes with_gs
    python -m experiments.run_judges --dry-run       # mostra quanti casi e stima i tempi
"""

from __future__ import annotations

import argparse
import time

from evaluation.advanced.judges import MAX_OUTPUT_TOKENS, OllamaJudge
from experiments import config
from experiments.common import (append_jsonl, fmt_seconds, gold_by_url, html_by_url,
                                load_cases, read_jsonl)


def select_cases(cases: list[dict], all_cases: bool) -> list[dict]:
    if all_cases:
        return cases
    return [c for c in cases
            if c["kind"] == "parser" or c["ptype"] == "none" or c["severity"] == config.JUDGE_SEVERITY]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--models", nargs="+", default=config.JUDGE_MODELS)
    ap.add_argument("--modes", nargs="+", default=config.JUDGE_MODES, choices=config.JUDGE_MODES)
    ap.add_argument("--all", action="store_true", help="giudica tutti i casi, non solo il sottoinsieme")
    ap.add_argument("--limit", type=int, default=None, help="massimo numero di casi (per prove)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cases = select_cases(load_cases(), args.all)
    if args.limit:
        cases = cases[:args.limit]
    gold = gold_by_url()
    html = html_by_url() if "without_gs" in args.modes else {}

    # gli errori "token repeat limit" sono deterministici (temperatura 0): non si ritentano.
    # Si rifanno invece i giudizi con risposte piu' lunghe di MAX_OUTPUT_TOKENS: sono stati
    # prodotti prima di introdurre il limite, cioe' con una configurazione diversa da quella finale.
    def is_done(r: dict) -> bool:
        if (r.get("output_tokens") or 0) > MAX_OUTPUT_TOKENS:
            return False
        return r.get("error", "") == "" or "repeat limit" in r.get("error", "")

    done = {(r["case_id"], r["model"], r["mode"]) for r in read_jsonl(config.JUDGES_PATH) if is_done(r)}
    jobs = [(c, m, mode) for m in args.models for mode in args.modes for c in cases
            if (c["case_id"], m, mode) not in done]
    print(f"Casi selezionati: {len(cases)} | modelli: {len(args.models)} | modalita': {args.modes}")
    print(f"Valutazioni da fare: {len(jobs)} (gia' fatte: {len(done)})")
    if args.dry_run or not jobs:
        return

    judges = {}
    for model in args.models:
        judge = OllamaJudge(model, host=config.OLLAMA_HOST, max_chars=config.JUDGE_MAX_CHARS,
                            num_ctx=config.JUDGE_NUM_CTX)
        if not judge.is_available():
            raise SystemExit(f"Modello '{model}' non disponibile su {config.OLLAMA_HOST}. "
                             f"Scaricalo con: ollama pull {model}")
        judges[model] = judge

    start = time.perf_counter()
    for i, (case, model, mode) in enumerate(jobs, start=1):
        result = judges[model].judge(mode, case["text"], gold_text=gold[case["url"]],
                                     html=html.get(case["url"], ""))
        row = {"case_id": case["case_id"], **result.to_dict()}
        append_jsonl(config.JUDGES_PATH, row)
        elapsed = time.perf_counter() - start
        eta = elapsed / i * (len(jobs) - i)
        status = f"score={result.score}" if result.valid_json else "JSON NON VALIDO"
        if result.error:
            status = f"ERRORE: {result.error[:60]}"
        print(f"[{i}/{len(jobs)}] {model:<15} {mode:<10} {case['case_id']:<36} {status} "
              f"({result.latency_s:.1f}s, fine tra ~{fmt_seconds(eta)})")

    print(f"Fatto. Risultati in {config.JUDGES_PATH}")


if __name__ == "__main__":
    main()
