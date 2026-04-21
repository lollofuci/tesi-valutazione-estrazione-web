from pathlib import Path
from urllib.parse import urlparse
import json
import re

from fastapi import FastAPI, HTTPException

from parsers.new_wikipedia_parser import WikipediaParser
from parsers.atptour_parser import ATPTourParser
from parsers.accuweather_parser import AccuWeatherParser
from parsers.accu_parser_eval import AccuWeatherEvalParser
from parsers.tradingeconomics_parser import TradingEconomicsParser

from models import (
    ParseResponse,
    DomainsResponse,
    GoldStandardEntry,
    FullGoldStandardResponse,
    EvalRequest,
    EvalResponse,
    ParseHtmlRequest,
)

from evaluation.evaluator import token_level_eval, aggregate_metrics


app = FastAPI()


# -------------------------
# PATH PROGETTO
# -------------------------

def find_project_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "domains.json").exists() and (candidate / "gs_data").exists():
            return candidate
    raise RuntimeError("Root del progetto non trovata: servono domains.json e gs_data/")


BASE_DIR = find_project_root(Path(__file__))
DOMAINS_PATH = BASE_DIR / "domains.json"
GS_DATA_DIR = BASE_DIR / "gs_data"


# -------------------------
# DOMAINS / GS
# -------------------------

def load_domains() -> list[str]:
    with open(DOMAINS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["domains"]


def normalize_domain(url_or_domain: str) -> str:
    domain = urlparse(url_or_domain).netloc or url_or_domain
    return domain.lower().removeprefix("www.")


def check_supported_domain(domain: str) -> None:
    normalized = normalize_domain(domain)
    supported_domains = load_domains()
    if normalized not in supported_domains:
        raise HTTPException(status_code=400, detail="Dominio non supportato")


def get_parser(domain: str):
    domain = normalize_domain(domain)

    if domain == "it.wikipedia.org":
        return WikipediaParser()
    if domain == "atptour.com":
        return ATPTourParser()
    if domain == "accuweather.com":
        return AccuWeatherParser()
    if domain == "tradingeconomics.com":
        return TradingEconomicsParser()

    raise HTTPException(status_code=400, detail="Dominio non supportato")


def get_gs_filename(domain: str) -> str:
    domain = normalize_domain(domain)

    if domain == "it.wikipedia.org":
        return "wikipedia_gs.json"
    if domain == "atptour.com":
        return "atptour_gs.json"
    if domain == "accuweather.com":
        return "accuweather.json"
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


# -------------------------
# MARKDOWN CLEANING
# -------------------------

def remove_markdown(text: str) -> str:
    """
    Rimuove in modo semplice la sintassi markdown più comune,
    senza usare BeautifulSoup o conversione HTML.
    """
    if not text:
        return ""

    cleaned = text

    # code block
    cleaned = re.sub(r"```.*?```", " ", cleaned, flags=re.DOTALL)

    # inline code
    cleaned = re.sub(r"`([^`]*)`", r"\1", cleaned)

    # immagini ![alt](url)
    cleaned = re.sub(r"!$begin:math:display$\(\[\^$end:math:display$]*)\]$begin:math:text$\[\^\)\]\+$end:math:text$", r"\1", cleaned)

    # link [testo](url)
    cleaned = re.sub(r"$begin:math:display$\(\[\^$end:math:display$]+)\]$begin:math:text$\[\^\)\]\+$end:math:text$", r"\1", cleaned)

    # heading
    cleaned = re.sub(r"^\s{0,3}#{1,6}\s*", "", cleaned, flags=re.MULTILINE)

    # blockquote
    cleaned = re.sub(r"^\s*>\s?", "", cleaned, flags=re.MULTILINE)

    # liste
    cleaned = re.sub(r"^\s*[-*+]\s+", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"^\s*\d+\.\s+", "", cleaned, flags=re.MULTILINE)

    # grassetto / corsivo
    cleaned = re.sub(r"\*\*(.*?)\*\*", r"\1", cleaned)
    cleaned = re.sub(r"__(.*?)__", r"\1", cleaned)
    cleaned = re.sub(r"\*(.*?)\*", r"\1", cleaned)
    cleaned = re.sub(r"_(.*?)_", r"\1", cleaned)

    # linee orizzontali
    cleaned = re.sub(r"^\s*---+\s*$", " ", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"^\s*\*\*\*+\s*$", " ", cleaned, flags=re.MULTILINE)

    # collapse spazi
    cleaned = re.sub(r"[ \t]+", " ", cleaned)
    cleaned = re.sub(r"\n+", "\n", cleaned)

    return cleaned.strip()


# -------------------------
# PARSING
# -------------------------

async def parse_with_best_parser(url: str) -> dict:
    domain = normalize_domain(url)
    check_supported_domain(domain)

    try:
        if domain == "accuweather.com":
            gs_entry = find_gs_entry(domain, url)
            if gs_entry is not None:
                parser = AccuWeatherEvalParser()
                return await parser.parse(url, gs_entry["html_text"])

            parser = AccuWeatherParser()
            return await parser.parse(url)

        parser = get_parser(domain)
        return await parser.parse(url)

    except HTTPException:
        raise
    except Exception as e:
        msg = str(e).lower()

        if (
            "crawl fallito" in msg
            or "timeout" in msg
            or "connection" in msg
            or "dns" in msg
            or "unreachable" in msg
            or "name resolution" in msg
        ):
            raise HTTPException(status_code=500, detail="URL irraggiungibile")

        raise HTTPException(status_code=500, detail=f"Errore nel parsing: {e}")


async def parse_from_html_with_correct_parser(url: str, html_text: str) -> dict:
    domain = normalize_domain(url)
    check_supported_domain(domain)

    parser = get_parser(domain)

    try:
        return await parser.parse_from_html(url, html_text)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore nel parsing: {e}")


# -------------------------
# ENDPOINTS
# -------------------------

@app.get("/domains", response_model=DomainsResponse)
def get_domains():
    return {"domains": load_domains()}


@app.get("/parse", response_model=ParseResponse)
async def parse_url(url: str):
    return await parse_with_best_parser(url)


@app.post("/parse", response_model=ParseResponse)
async def parse_html(req: ParseHtmlRequest):
    return await parse_from_html_with_correct_parser(req.url, req.html_text)


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
    parsed_clean = remove_markdown(req.parsed_text).lower()
    gold_clean = req.gold_text.strip().lower()

    metrics = token_level_eval(parsed_clean, gold_clean)

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

    for entry in gs:
        parsed_result = await parse_with_best_parser(entry["url"])
        parsed_clean = remove_markdown(parsed_result["parsed_text"]).lower()
        gold_clean = entry["gold_text"].strip().lower()

        metrics = token_level_eval(parsed_clean, gold_clean)
        metrics_list.append(metrics)

    final_metrics = aggregate_metrics(metrics_list)

    return {
        "token_level_eval": final_metrics,
        "x_eval": {}
    }