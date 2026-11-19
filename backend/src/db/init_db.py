"""Inizializzazione del database: crea le tabelle, popola il GS dai JSON e
pre-calcola le valutazioni. Eseguibile come modulo: python -m db.init_db
"""

import asyncio
import json
import os
from pathlib import Path

from db.connection import get_connection, wait_for_db
from db import repository

SCHEMA_PATH = Path(__file__).with_name("schema.sql")


def find_gs_dir() -> Path | None:
    """Cerca la cartella gs_data (nel container e in locale)."""
    here = Path(__file__).resolve()
    for candidate in (here.parents[2] / "gs_data", here.parents[3] / "gs_data"):
        if candidate.is_dir():
            return candidate
    return None


def create_tables(conn) -> None:
    sql = SCHEMA_PATH.read_text(encoding="utf-8")
    statements = [s.strip() for s in sql.split(";") if s.strip()]
    cur = conn.cursor()
    for statement in statements:
        cur.execute(statement)
    conn.commit()
    cur.close()
    print(f"[db] tabelle create/verificate ({len(statements)} statement)")


def load_gs_files() -> list[dict]:
    gs_dir = find_gs_dir()
    if gs_dir is None:
        print("[db] cartella gs_data non trovata, nessun popolamento")
        return []
    entries: list[dict] = []
    for json_file in sorted(gs_dir.glob("*_gs.json")):
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            entries.extend(data)
        print(f"[db] letto {json_file.name}: {len(data)} entry")
    return entries


def populate(conn, entries: list[dict]) -> None:
    cur = conn.cursor()
    insert_resource = (
        "INSERT INTO web_resources (url, domain, title, html_text) VALUES (?, ?, ?, ?) "
        "ON DUPLICATE KEY UPDATE domain=VALUES(domain), title=VALUES(title), html_text=VALUES(html_text)"
    )
    insert_gold = (
        "INSERT INTO gold_standard (url, gold_text) VALUES (?, ?) "
        "ON DUPLICATE KEY UPDATE gold_text=VALUES(gold_text)"
    )
    inserted = 0
    for entry in entries:
        url = entry.get("url")
        if not url:
            continue
        cur.execute(insert_resource,
                    (url, entry.get("domain", ""), entry.get("title", ""), entry.get("html_text", "")))
        cur.execute(insert_gold, (url, entry.get("gold_text", "")))
        inserted += 1
    conn.commit()
    cur.close()
    print(f"[db] popolate {inserted} entry in web_resources/gold_standard")


def _build_parser(domain: str):
    from parsers.wikipedia_parser import WikipediaParser
    from parsers.atptour_parser import ATPTourParser
    from parsers.accuweather_parser import AccuWeatherParser
    from parsers.tradingeconomics_parser import TradingEconomicsParser

    mapping = {
        "it.wikipedia.org": WikipediaParser,
        "www.atptour.com": ATPTourParser,
        "www.accuweather.com": AccuWeatherParser,
        "tradingeconomics.com": TradingEconomicsParser,
    }
    parser_cls = mapping.get(domain)
    return parser_cls() if parser_cls else None


def _evaluations_already_present() -> bool:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM evaluations")
        n_eval = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM judge_evaluations")
        n_judge = cur.fetchone()[0]
        cur.close()
        return n_eval > 0 and n_judge > 0
    finally:
        conn.close()


async def _precompute(entries: list[dict]) -> None:
    """Per ogni entry: parsing dell'HTML salvato, token-eval e judge, salvati nel DB."""
    from evaluation.evaluator import token_level_eval
    from evaluation.judge import evaluate_judge as run_judge

    done = 0
    for entry in entries:
        url = entry.get("url")
        parser = _build_parser(entry.get("domain", ""))
        if parser is None or not url:
            continue
        try:
            result = await parser.parse_from_html(url, entry.get("html_text", ""))
            parsed_text = result.get("parsed_text", "")
            repository.save_parsed_document(url, result.get("title", ""), parsed_text)
            metrics = token_level_eval(parsed_text, entry.get("gold_text", ""))
            repository.save_evaluation(url, metrics["precision"], metrics["recall"], metrics["f1"])
            judge = run_judge(parsed_text, entry.get("gold_text", ""))
            repository.save_judge_evaluation(url, judge["model_name"], judge["judge_score"], judge["judge_feedback"])
            done += 1
            print(f"[db] pre-calcolo {done}: {url[:60]} f1={metrics['f1']:.3f} judge={judge['judge_score']}")
        except Exception as exc:
            print(f"[db] pre-calcolo fallito per {url}: {exc}")
    print(f"[db] pre-calcolo completato: {done}/{len(entries)} entry")


def _advanced_evaluations_present() -> bool:
    """Tesi: True se le metriche avanzate sono gia' state calcolate per qualche pagina."""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM advanced_evaluations")
        n = cur.fetchone()[0]
        cur.close()
        return n > 0
    finally:
        conn.close()


async def _precompute_advanced(entries: list[dict]) -> None:
    """Tesi (personalizzazione 4a): metriche avanzate di ogni pagina del GS, salvate nel DB.

    Solo ROUGE-L, chrF e METEOR, che richiedono millisecondi; BERTScore no, perche'
    caricherebbe all'avvio un modello da circa 700 MB (si calcola dalla pagina
    "Valutazione avanzata").
    """
    from advanced_api import compute_advanced_metrics

    done = 0
    for entry in entries:
        url = entry.get("url")
        parser = _build_parser(entry.get("domain", ""))
        if parser is None or not url:
            continue
        try:
            result = await parser.parse_from_html(url, entry.get("html_text", ""))
            metrics = compute_advanced_metrics(result.get("parsed_text", ""), entry.get("gold_text", ""))
            repository.save_advanced_evaluation(url, metrics)
            done += 1
        except Exception as exc:
            print(f"[db] metriche avanzate non calcolate per {url}: {exc}")
    print(f"[db] metriche avanzate pre-calcolate: {done}/{len(entries)} entry")


def run_precompute_if_needed() -> None:
    """Pre-calcolo delle valutazioni, chiamato in background dal backend all'avvio."""
    if os.getenv("PRECOMPUTE_STATS", "1") == "0":
        return
    entries = None
    # Tesi: prima le metriche avanzate, che richiedono pochi secondi
    if not _advanced_evaluations_present():
        entries = load_gs_files()
        if entries:
            asyncio.run(_precompute_advanced(entries))
    if _evaluations_already_present():
        print("[db] valutazioni gia' presenti, salto il pre-calcolo")
        return
    entries = entries or load_gs_files()
    if entries:
        print(f"[db] pre-calcolo su {len(entries)} entry (in background)...")
        asyncio.run(_precompute(entries))


def main() -> None:
    wait_for_db()
    conn = get_connection(autocommit=False)
    try:
        create_tables(conn)
        entries = load_gs_files()
        populate(conn, entries)
    finally:
        conn.close()
    print("[db] inizializzazione completata (tabelle + gold standard).")


if __name__ == "__main__":
    main()
