from pathlib import Path
from urllib.parse import urlparse
import json
import os
import urllib.request

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from parsers.wikipedia_parser import WikipediaParser
from parsers.atptour_parser import ATPTourParser
from parsers.accuweather_parser import AccuWeatherParser
from parsers.tradingeconomics_parser import TradingEconomicsParser
from models import (ParseResponse,DomainsResponse,GoldStandardEntry,FullGoldStandardResponse,EvalRequest,EvalResponse,ParseHtmlRequest,ParseRequest,JudgeResponse,FullGsEvalResponse)
from evaluation.evaluator import token_level_eval, aggregate_metrics
from evaluation.judge import evaluate_judge as run_judge
from db import connection, repository, init_db
from advanced_api import router as advanced_router, x_eval_summary

app = FastAPI()
# Tesi (personalizzazione 4a): endpoint della valutazione avanzata
app.include_router(advanced_router)


@app.on_event("startup")
def _start_background_precompute() -> None:
    """Avvia in background il pre-calcolo delle valutazioni (non blocca l'avvio)."""
    import threading

    threading.Thread(
        target=init_db.run_precompute_if_needed, daemon=True
    ).start()

BASE_DIR = Path(__file__).parent.parent.resolve()
DOMAINS_PATH = BASE_DIR / "domains.json"

def load_domains() -> list[str]:
    with open(DOMAINS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["domains"]

def normalize_domain(url_or_domain: str) -> str:
    if not url_or_domain.startswith(("http://", "https://")):
        url_or_domain = "https://" + url_or_domain
    domain = urlparse(url_or_domain).netloc
    return domain.lower()

def check_supported_domain(domain: str) -> None:
    normalized = normalize_domain(domain)
    supported_domains = load_domains()
    if normalized not in supported_domains:
        raise HTTPException(status_code=400, detail="Dominio non supportato")

def get_parser(domain: str):
    domain = normalize_domain(domain)
    if domain == "it.wikipedia.org":
        return WikipediaParser()
    if domain == "www.atptour.com":
        return ATPTourParser()
    if domain == "www.accuweather.com":
        return AccuWeatherParser()
    if domain == "tradingeconomics.com":
        return TradingEconomicsParser()
    raise HTTPException(status_code=400, detail="Dominio non supportato")

def get_eval_parser(domain: str):
    return get_parser(domain)


class AddWebResourceRequest(BaseModel):
    url: str
    html_text: str

class AddGoldStandardRequest(BaseModel):
    url: str
    gold_text: str

class UrlRequest(BaseModel):
    url: str


@app.get("/domains", response_model=DomainsResponse)
def get_domains():
    return {"domains": load_domains()}

@app.get("/parse", response_model=ParseResponse)
async def parse_url(url: str):
    domain = normalize_domain(url)
    check_supported_domain(domain)
    try:
        parser = get_parser(domain)
        return await parser.parse(url)
    except HTTPException:
        raise
    except Exception as e:
        msg = str(e).lower()
        if any(err in msg for err in ["crawl fallito", "timeout", "connection", "dns", "unreachable", "name resolution"]):
            raise HTTPException(status_code=500, detail="URL irraggiungibile")
        raise HTTPException(status_code=500, detail=f"Errore nel parsing: {e}")

@app.post("/parse", response_model=ParseResponse)
async def parse_post(req: ParseRequest):
    domain = normalize_domain(req.url)
    check_supported_domain(domain)
    parser = get_parser(domain)
    try:
        if req.local:  # usa l'HTML salvato nel DB, senza scaricare
            resource = repository.get_web_resource(req.url)
            if resource is None:
                raise HTTPException(status_code=404, detail="URL non nel DB")
            return await parser.parse_from_html(req.url, resource.get("html_text", ""))
        return await parser.parse(req.url)
    except HTTPException:
        raise
    except Exception as e:
        msg = str(e).lower()
        if any(err in msg for err in ["crawl fallito", "timeout", "connection", "dns", "unreachable", "name resolution"]):
            raise HTTPException(status_code=500, detail="URL irraggiungibile")
        raise HTTPException(status_code=500, detail=f"Errore nel parsing: {e}")

@app.get("/gold_standard", response_model=GoldStandardEntry)
def get_gold_standard(url: str):
    # Se l'URL non e' nel DB -> 404 (copre anche i domini non supportati).
    entry = repository.get_gold_standard_entry(url)
    if entry is None:
        raise HTTPException(status_code=404, detail="URL non nel GS")
    return entry

@app.get("/full_gold_standard", response_model=FullGoldStandardResponse)
def get_full_gold_standard(domain: str):
    normalized_domain = normalize_domain(domain)
    check_supported_domain(normalized_domain)
    gs = repository.get_full_gold_standard(normalized_domain)
    return {"gold_standard": gs}

@app.post("/evaluate", response_model=EvalResponse)
def evaluate(req: EvalRequest):
    metrics = token_level_eval(req.parsed_text, req.gold_text)
    # x_eval: valutazioni aggiuntive (tesi): F-score di ROUGE-L, chrF e METEOR
    try:
        x_eval = x_eval_summary(req.parsed_text, req.gold_text)
    except Exception:
        x_eval = {}
    return {
        "token_level_eval": metrics,
        "x_eval": x_eval
    }

@app.get("/full_gs_eval", response_model=FullGsEvalResponse)
async def full_gs_eval(domain: str):
    normalized_domain = normalize_domain(domain)
    check_supported_domain(normalized_domain)

    gs = repository.get_full_gold_standard(normalized_domain)
    metrics_list = []
    parser = get_eval_parser(normalized_domain)

    for entry in gs:
        try:
            parsed_result = await parser.parse_from_html(entry["url"], entry.get("html_text", ""))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Errore nel parsing del GS per URL {entry['url']}: {e}")

        metrics = token_level_eval(parsed_result["parsed_text"], entry["gold_text"])
        metrics_list.append(metrics)
        try:
            repository.save_evaluation(
                entry["url"], metrics["precision"], metrics["recall"], metrics["f1"]
            )
        except Exception:
            pass

    final_metrics = aggregate_metrics(metrics_list)
    # judge_score letto dal DB (gia' pre-calcolato), non ricalcolato via LLM.
    avg_judge = repository.avg_judge_for_domain(normalized_domain)

    return {
        "token_level_eval": final_metrics,
        "judge_score": round(avg_judge, 4),
        "x_eval": {}
    }


@app.post("/evaluate_judge", response_model=JudgeResponse)
def evaluate_judge(req: EvalRequest):
    return run_judge(req.parsed_text, req.gold_text)


@app.get("/gold_standard_urls")
def get_gold_standard_urls(domain: str):
    normalized_domain = normalize_domain(domain)
    check_supported_domain(normalized_domain)
    return {"gold_standard_urls": repository.get_gold_standard_urls(normalized_domain)}

@app.post("/add_web_resource")
def add_web_resource(req: AddWebResourceRequest):
    try:
        domain = normalize_domain(req.url)
        title = repository.get_web_resource(req.url)
        existing_title = title["title"] if title else ""
        repository.add_web_resource(req.url, domain, existing_title or "", req.html_text)
        return {"status": "ok"}
    except Exception:
        return {"status": "error"}

@app.post("/add_gold_standard")
def add_gold_standard(req: AddGoldStandardRequest):
    try:
        repository.add_gold_standard(req.url, req.gold_text)
        return {"status": "ok"}
    except LookupError:
        return {"status": "error"}
    except Exception:
        return {"status": "error"}

@app.delete("/web_resource")
def delete_web_resource(req: UrlRequest):
    try:
        removed = repository.delete_web_resource(req.url)
        return {"status": "ok"} if removed else {"status": "error"}
    except Exception:
        return {"status": "error"}

@app.delete("/gold_standard")
def delete_gold_standard(req: UrlRequest):
    try:
        removed = repository.delete_gold_standard(req.url)
        return {"status": "ok"} if removed else {"status": "error"}
    except Exception:
        return {"status": "error"}

@app.get("/db_stats")
def db_stats():
    web_counts, gs_counts = repository.count_per_domain()
    avg_eval = repository.avg_eval_per_domain()
    avg_judge = repository.avg_judge_per_domain()
    try:
        avg_advanced = repository.avg_advanced_per_domain()
    except Exception:
        avg_advanced = {}

    # Garantisce una entry (anche a zero) per ogni dominio di web_resources.
    for domain in web_counts:
        avg_eval.setdefault(
            domain, {"token_level_eval": {"precision": 0.0, "recall": 0.0, "f1": 0.0}}
        )
        avg_judge.setdefault(domain, {"judge_score": 0.0})

    return {
        "web_resources": web_counts,
        "gold_standard": gs_counts,
        "avg_eval": avg_eval,
        "avg_eval_judge": avg_judge,
        "avg_advanced": avg_advanced,
    }

@app.get("/db_schema")
def db_schema():
    return repository.get_db_schema()

@app.get("/status")
def status():
    return {
        "backend": "ok",
        "database": "ok" if connection.is_alive() else "error",
        "ollama": "ok" if _ollama_alive() else "error",
    }


def _ollama_alive() -> bool:
    """True se Ollama risponde (per /status)."""
    base_url = os.getenv("OLLAMA_HOST", "http://ollama:11434")
    try:
        with urllib.request.urlopen(f"{base_url}/api/tags", timeout=1.5) as resp:
            return resp.status == 200
    except Exception:
        return False
