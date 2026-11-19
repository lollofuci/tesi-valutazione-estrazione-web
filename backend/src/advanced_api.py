"""API REST della valutazione avanzata (personalizzazione 4a della tesi).

Endpoint aggiunti al backend del progetto base:
- POST /advanced_evaluate       metriche avanzate tra testo estratto e Gold Standard
- GET  /judge_models            modelli disponibili per il giudice LLM
- POST /advanced_judge          giudice LLM a scelta, con o senza Gold Standard
- GET  /full_gs_advanced_eval   metriche avanzate su tutto il GS di un dominio (salvate nel DB)
- GET  /experiment_results      risultati degli esperimenti della tesi (results/summary.json)
- GET  /experiment_figure/{n}   grafici degli esperimenti (PNG)
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import requests
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from db import repository
from evaluation.advanced.judges import OllamaJudge
from evaluation.advanced.metrics import lexical_metrics
from evaluation.advanced.text_utils import detect_language

router = APIRouter()

RESULTS_DIR = Path(os.getenv("RESULTS_DIR", Path(__file__).resolve().parent.parent / "results"))
# Ollama per i giudici avanzati: di default quello installato sul Mac (piu' veloce e con piu'
# modelli); se non risponde si usa quello del progetto base.
ADVANCED_OLLAMA_HOST = os.getenv("ADVANCED_OLLAMA_HOST", "")
DEFAULT_OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://ollama:11434")

LEXICAL_METRICS = ("token", "rougeL", "chrf", "meteor")
JUDGE_MODES = ("with_gs", "without_gs")

_bert_scorer = None


# ---------------------------------------------------------------------------
# Modelli di input
# ---------------------------------------------------------------------------

class AdvancedEvalRequest(BaseModel):
    parsed_text: str
    gold_text: str
    bertscore: bool = False


class AdvancedJudgeRequest(BaseModel):
    parsed_text: str
    model: str
    mode: str = "with_gs"
    gold_text: str = ""
    url: str = ""          # modalita' without_gs: l'HTML della pagina viene letto dal DB


# ---------------------------------------------------------------------------
# Funzioni di supporto
# ---------------------------------------------------------------------------

def _get_bert_scorer():
    """BERTScore viene caricato solo alla prima richiesta (modello di circa 700 MB)."""
    global _bert_scorer
    if _bert_scorer is None:
        from evaluation.advanced.bertscore import LongBertScorer
        _bert_scorer = LongBertScorer()
    return _bert_scorer


def compute_advanced_metrics(parsed_text: str, gold_text: str, bertscore: bool = False) -> dict:
    """{metrica: {precision, recall, f}} per tutte le metriche avanzate."""
    flat = lexical_metrics(parsed_text, gold_text, lang=detect_language(gold_text))
    result = {
        name: {
            "precision": round(flat[f"{name}_precision"], 4),
            "recall": round(flat[f"{name}_recall"], 4),
            "f": round(flat[f"{name}_f"], 4),
        }
        for name in LEXICAL_METRICS
    }
    if bertscore:
        scores = _get_bert_scorer().score(parsed_text, gold_text)
        result["bertscore"] = {k: round(v, 4) for k, v in scores.items()}
    return result


def x_eval_summary(parsed_text: str, gold_text: str) -> dict:
    """F-score delle metriche avanzate (senza BERTScore), usato nel campo x_eval di /evaluate."""
    metrics = compute_advanced_metrics(parsed_text, gold_text)
    return {f"{name}_f": metrics[name]["f"] for name in LEXICAL_METRICS if name != "token"}


def _ollama_models(host: str) -> list[str] | None:
    try:
        response = requests.get(f"{host.rstrip('/')}/api/tags", timeout=3)
        response.raise_for_status()
        return sorted(m.get("name", "") for m in response.json().get("models", []))
    except (requests.RequestException, ValueError):
        return None


def judge_host() -> tuple[str, list[str]]:
    """Primo Ollama raggiungibile e i suoi modelli."""
    for host in (ADVANCED_OLLAMA_HOST, DEFAULT_OLLAMA_HOST):
        if host:
            models = _ollama_models(host)
            if models is not None:
                return host, models
    return "", []


# ---------------------------------------------------------------------------
# Endpoint
# ---------------------------------------------------------------------------

@router.post("/advanced_evaluate")
def advanced_evaluate(req: AdvancedEvalRequest):
    if not req.gold_text.strip():
        raise HTTPException(status_code=400, detail="gold_text vuoto")
    return {
        "language": detect_language(req.gold_text),
        "metrics": compute_advanced_metrics(req.parsed_text, req.gold_text, req.bertscore),
    }


@router.get("/judge_models")
def judge_models():
    host, models = judge_host()
    return {"host": host, "models": models, "modes": list(JUDGE_MODES)}


@router.post("/advanced_judge")
def advanced_judge(req: AdvancedJudgeRequest):
    if req.mode not in JUDGE_MODES:
        raise HTTPException(status_code=400, detail=f"Modalità non valida: usare {JUDGE_MODES}")
    host, models = judge_host()
    if not host:
        raise HTTPException(status_code=503, detail="Ollama non raggiungibile")
    if req.model not in models and f"{req.model}:latest" not in models:
        raise HTTPException(status_code=404, detail=f"Modello '{req.model}' non disponibile su {host}")

    html = ""
    if req.mode == "without_gs":
        resource = repository.get_web_resource(req.url) if req.url else None
        if resource is None:
            raise HTTPException(status_code=404, detail="URL non nel DB: serve l'HTML della pagina")
        html = resource.get("html_text") or ""
    elif not req.gold_text.strip():
        raise HTTPException(status_code=400, detail="gold_text vuoto (modalità con Gold Standard)")

    result = OllamaJudge(req.model, host=host).judge(req.mode, req.parsed_text,
                                                    gold_text=req.gold_text, html=html)
    if result.error and not result.valid_json and "repeat limit" not in result.error:
        raise HTTPException(status_code=502, detail=f"Errore del modello: {result.error[:200]}")
    data = result.to_dict()
    # la risposta grezza si restituisce solo se non e' un JSON valido: serve a capire l'errore
    if result.valid_json:
        data.pop("raw", None)
    return data


@router.get("/full_gs_advanced_eval")
async def full_gs_advanced_eval(domain: str, bertscore: bool = False):
    # import ritardato: server importa questo modulo
    from server import check_supported_domain, get_eval_parser, normalize_domain

    normalized = normalize_domain(domain)
    check_supported_domain(normalized)
    parser = get_eval_parser(normalized)

    documents = []
    for entry in repository.get_full_gold_standard(normalized):
        try:
            parsed = await parser.parse_from_html(entry["url"], entry.get("html_text", ""))
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Errore nel parsing di {entry['url']}: {exc}")
        metrics = compute_advanced_metrics(parsed["parsed_text"], entry["gold_text"], bertscore)
        try:
            repository.save_advanced_evaluation(entry["url"], metrics)
        except Exception:
            pass
        documents.append({"url": entry["url"], **{f"{k}_f": v["f"] for k, v in metrics.items()}})

    keys = [k for k in documents[0] if k != "url"] if documents else []
    average = {k: round(sum(d[k] for d in documents) / len(documents), 4) for k in keys}
    return {"domain": normalized, "documents": documents, "average": average}


@router.get("/experiment_results")
def experiment_results():
    path = RESULTS_DIR / "summary.json"
    if not path.exists():
        raise HTTPException(status_code=404,
                            detail="Risultati non trovati: eseguire prima gli esperimenti (experiments.analyze)")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    figures_dir = RESULTS_DIR / "figures"
    data["figures"] = sorted(p.name for p in figures_dir.glob("*.png")) if figures_dir.exists() else []
    return data


@router.get("/experiment_figure/{name}")
def experiment_figure(name: str):
    path = RESULTS_DIR / "figures" / name
    # solo file PNG dentro results/figures (niente percorsi arbitrari)
    if Path(name).name != name or path.suffix != ".png" or not path.exists():
        raise HTTPException(status_code=404, detail="Figura non trovata")
    return FileResponse(path, media_type="image/png")
