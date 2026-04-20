from pathlib import Path
from urllib.parse import urlparse
import json

from fastapi import FastAPI, HTTPException

from parsers.new_wikipedia_parser import WikipediaParser
from parsers.atptour_parser import ATPTourParser
from parsers.accuweather_parser import AccuWeatherParser
from parsers.tradingeconomics_parser import TradingEconomicsParser
from models import (
    ParseResponse,
    DomainsResponse,
    GoldStandardEntry,
    FullGoldStandardResponse,
    EvalRequest,
    EvalResponse,
)
from evaluation.evaluator import token_level_eval, aggregate_metrics


app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent
DOMAINS_PATH = BASE_DIR / "domains.json"
GS_DATA_DIR = BASE_DIR / "gs_data"


# -------------------------
# DOMAINS
# -------------------------

def load_domains() -> list[str]:
    with open(DOMAINS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["domains"]


@app.get("/domains", response_model=DomainsResponse)
def get_domains():
    return {"domains": load_domains()}


def check_supported_domain(domain: str) -> None:
    supported_domains = load_domains()
    if domain not in supported_domains:
        raise HTTPException(status_code=400, detail="Dominio non supportato")


# -------------------------
# PARSER
# -------------------------

def get_parser(domain: str):
    if domain == "it.wikipedia.org":
        return WikipediaParser()
    if domain == "atptour.com":
        return ATPTourParser()
    if domain == "accuweather.com":
        return AccuWeatherParser()
    if domain == "tradingeconomics.com":
        return TradingEconomicsParser()
    raise HTTPException(status_code=400, detail="Dominio non supportato")


def normalize_domain(url_or_domain: str) -> str:
    domain = urlparse(url_or_domain).netloc or url_or_domain
    return domain.lower().removeprefix("www.")


def check_supported_domain(domain: str) -> None:
    domain = normalize_domain(domain)
    supported_domains = load_domains()
    if domain not in supported_domains:
        raise HTTPException(status_code=400, detail="Dominio non supportato")


@app.get("/parse", response_model=ParseResponse)
async def parse_url(url: str):
    domain = normalize_domain(url)
    check_supported_domain(domain)

    parser = get_parser(domain)

    try:
        result = await parser.parse(url)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore nel parsing: {e}")


@app.get("/gold_standard", response_model=GoldStandardEntry)
def get_gs(url: str):
    domain = normalize_domain(url)
    check_supported_domain(domain)

    gs = load_gs(domain)

    for entry in gs:
        if entry["url"] == url:
            return entry

    raise HTTPException(status_code=404, detail="URL non nel GS")

# -------------------------
# GOLD STANDARD
# -------------------------

def get_gs_filename(domain: str) -> str:
    if domain == "it.wikipedia.org":
        return "wikipedia_gs.json"
    if domain == "atptour.com":
        return "atptour_gs.json"
    if domain == "accuweather.com":
        return "accuweather.json"
    if domain == "tradingeconomics.com":
        return "tradingeconomics_gs.json"
    raise HTTPException(status_code=400, detail="Dominio non supportato")


def load_gs(domain: str):
    filename = get_gs_filename(domain)
    gs_path = GS_DATA_DIR / filename

    try:
        with open(gs_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="File GS non trovato")



@app.get("/full_gold_standard", response_model=FullGoldStandardResponse)
def get_full_gs(domain: str):
    check_supported_domain(domain)
    gs = load_gs(domain)
    return {"gold_standard": gs}


# -------------------------
# EVALUATION
# -------------------------

@app.post("/evaluate", response_model=EvalResponse)
def evaluate(req: EvalRequest):
    metrics = token_level_eval(req.parsed_text, req.gold_text)

    return {
        "token_level_eval": metrics,
        "x_eval": {}
    }


@app.get("/full_gs_eval", response_model=EvalResponse)
async def full_eval(domain: str):
    check_supported_domain(domain)

    gs = load_gs(domain)
    parser = get_parser(domain)

    metrics_list = []

    for entry in gs:
        parsed = await parser.parse(entry["url"])
        metrics = token_level_eval(parsed["parsed_text"], entry["gold_text"])
        metrics_list.append(metrics)

    final_metrics = aggregate_metrics(metrics_list)

    return {
        "token_level_eval": final_metrics,
        "x_eval": {}
    }