from pathlib import Path
from urllib.parse import urlparse
import json
import re
import html
from fastapi import FastAPI, HTTPException
from parsers.wikipedia_parser import WikipediaParser
from parsers.atptour_parser import ATPTourParser
from parsers.accuweather_parser import AccuWeatherParser
from parsers.tradingeconomics_parser import TradingEconomicsParser
from models import (ParseResponse,DomainsResponse,GoldStandardEntry,FullGoldStandardResponse,EvalRequest,EvalResponse,ParseHtmlRequest)
from evaluation.evaluator import token_level_eval, aggregate_metrics

app = FastAPI()

BASE_DIR = Path(__file__).parent.parent.resolve()
DOMAINS_PATH = BASE_DIR / "domains.json"
GS_DATA_DIR = BASE_DIR / "gs_data"

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

def get_gs_filename(domain: str) -> str:
    domain = normalize_domain(domain)
    if domain == "it.wikipedia.org":
        return "wikipedia_gs.json"
    if domain == "www.atptour.com":
        return "atptour_gs.json"
    if domain == "www.accuweather.com":
        return "accuweather_gs.json"
    if domain == "tradingeconomics.com":
        return "tradingeconomics_gs.json"
    raise HTTPException(status_code=400, detail="Dominio non supportato")

def load_gs(domain: str) -> list[dict]:
    filename = get_gs_filename(domain)
    gs_path = GS_DATA_DIR / filename
    try:
        with open(gs_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="File GS non trovato")

def find_gs_entry(domain: str, url: str) -> dict | None:
    gs = load_gs(domain)
    for entry in gs:
        if entry["url"] == url:
            return entry
    return None

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
async def parse_html(req: ParseHtmlRequest):
    domain = normalize_domain(req.url)
    check_supported_domain(domain)
    parser = get_parser(domain)
    try:
        return await parser.parse_from_html(req.url, req.html_text)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore nel parsing HTML: {e}")

@app.get("/gold_standard", response_model=GoldStandardEntry)
def get_gold_standard(url: str):
    domain = normalize_domain(url)
    check_supported_domain(domain)
    entry = find_gs_entry(domain, url)
    if entry is None:
        raise HTTPException(status_code=404, detail="URL non nel GS")
    return entry

@app.get("/full_gold_standard", response_model=FullGoldStandardResponse)
def get_full_gold_standard(domain: str):
    normalized_domain = normalize_domain(domain)
    check_supported_domain(normalized_domain)
    gs = load_gs(normalized_domain)
    return {"gold_standard": gs}

@app.post("/evaluate", response_model=EvalResponse)
def evaluate(req: EvalRequest):
    metrics = token_level_eval(req.parsed_text, req.gold_text)
    return {
        "token_level_eval": metrics,
        "x_eval": {}
    }

@app.get("/full_gs_eval", response_model=EvalResponse)
async def full_gs_eval(domain: str):
    normalized_domain = normalize_domain(domain)
    check_supported_domain(normalized_domain)

    gs = load_gs(normalized_domain)
    metrics_list = []
    parser = get_eval_parser(normalized_domain)

    for entry in gs:
        try:
            parsed_result = await parser.parse_from_html(entry["url"], entry.get("html_text", ""))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Errore nel parsing del GS per URL {entry['url']}: {e}")

        metrics = token_level_eval(parsed_result["parsed_text"], entry["gold_text"])
        metrics_list.append(metrics)

    final_metrics = aggregate_metrics(metrics_list)

    return {
        "token_level_eval": final_metrics,
        "x_eval": {}
    }