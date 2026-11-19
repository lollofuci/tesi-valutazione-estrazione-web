import os

import requests
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8003")

# Membri del gruppo (mostrati nella home).
STUDENTS = [
    {"nome": "Matteo Mercieri", "matricola": "2100891"},
    {"nome": "Emiliano Frioni", "matricola": "2135576"},
    {"nome": "Lorenzo Augusto Fucito", "matricola": "2134663"},
]


def get_domains() -> list[str]:
    try:
        r = requests.get(f"{BACKEND_URL}/domains", timeout=60)
        if r.status_code == 200:
            return r.json().get("domains", [])
    except requests.RequestException:
        pass
    return []


def get_status() -> dict:
    try:
        r = requests.get(f"{BACKEND_URL}/status", timeout=60)
        if r.status_code == 200:
            return r.json()
    except requests.RequestException:
        pass
    return {"backend": "error", "database": "error", "ollama": "error"}


def get_gs_urls(domain: str) -> list[str]:
    try:
        r = requests.get(f"{BACKEND_URL}/gold_standard_urls", params={"domain": domain}, timeout=60)
        if r.status_code == 200:
            return r.json().get("gold_standard_urls", [])
    except requests.RequestException:
        pass
    return []


def get_all_gs_urls() -> list[str]:
    urls: list[str] = []
    for domain in get_domains():
        urls.extend(get_gs_urls(domain))
    return sorted(set(urls))


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "active": "home",
            "students": STUDENTS,
            "status": get_status(),
            "domains": get_domains(),
        },
    )


@app.get("/parser", response_class=HTMLResponse)
def parser_page(request: Request):
    return templates.TemplateResponse(
        request,
        "parser.html",
        {"active": "parser", "gs_urls": get_all_gs_urls()},
    )


@app.post("/parser", response_class=HTMLResponse)
def parser_run(request: Request, url: str = Form(""), gs_url: str = Form(""), mode: str = Form("live")):
    target_url = (url or gs_url).strip()
    is_local = mode == "local"
    parse_data = gold_data = eval_data = judge_data = None
    error = None

    ctx = {"active": "parser", "gs_urls": get_all_gs_urls(), "selected_url": target_url, "mode": mode}

    if not target_url:
        ctx["error"] = "Inserisci un URL o selezionane uno dal Gold Standard."
        return templates.TemplateResponse(request, "parser.html", ctx)

    try:
        r = requests.post(f"{BACKEND_URL}/parse", json={"url": target_url, "local": is_local}, timeout=180)
        if r.status_code != 200:
            error = f"Errore nel parsing ({r.status_code}): {r.json().get('detail', r.text)}"
        else:
            parse_data = r.json()
            # Se l'URL e' nel GS, confronta e valuta.
            g = requests.get(f"{BACKEND_URL}/gold_standard", params={"url": target_url}, timeout=120)
            if g.status_code == 200:
                gold_data = g.json()
                ev = requests.post(
                    f"{BACKEND_URL}/evaluate",
                    json={"parsed_text": parse_data["parsed_text"], "gold_text": gold_data["gold_text"]},
                    timeout=120,
                )
                if ev.status_code == 200:
                    eval_data = ev.json()
                jd = requests.post(
                    f"{BACKEND_URL}/evaluate_judge",
                    json={"parsed_text": parse_data["parsed_text"], "gold_text": gold_data["gold_text"]},
                    timeout=180,
                )
                if jd.status_code == 200:
                    judge_data = jd.json()
    except requests.RequestException as exc:
        error = f"Errore di comunicazione con il backend: {exc}"

    ctx.update({
        "parse_data": parse_data, "gold_data": gold_data,
        "eval_data": eval_data, "judge_data": judge_data, "error": error,
    })
    return templates.TemplateResponse(request, "parser.html", ctx)


def _gs_context(selected_domain: str, **extra) -> dict:
    domains = get_domains()
    if not selected_domain and domains:
        selected_domain = domains[0]
    ctx = {
        "active": "gold",
        "domains": domains,
        "selected_domain": selected_domain,
        "gs_urls": get_gs_urls(selected_domain) if selected_domain else [],
        "loaded_html": None,
    }
    ctx.update(extra)
    return ctx


@app.get("/gold-standard", response_class=HTMLResponse)
def gold_page(request: Request, domain: str = ""):
    return templates.TemplateResponse(request, "gold_standard.html", _gs_context(domain))


@app.post("/gold-standard/load", response_class=HTMLResponse)
def gold_load(request: Request, domain: str = Form(...), url: str = Form(...)):
    error = None
    loaded_html = None
    try:
        r = requests.post(f"{BACKEND_URL}/parse", json={"url": url.strip(), "local": False}, timeout=180)
        if r.status_code == 200:
            loaded_html = r.json().get("html_text", "")
        else:
            error = f"Impossibile scaricare l'HTML ({r.status_code}): {r.json().get('detail', r.text)}"
    except requests.RequestException as exc:
        error = f"Errore di comunicazione con il backend: {exc}"

    ctx = _gs_context(domain, loaded_url=url.strip(), loaded_html=loaded_html, error=error)
    return templates.TemplateResponse(request, "gold_standard.html", ctx)


@app.post("/gold-standard/save", response_class=HTMLResponse)
def gold_save(request: Request, domain: str = Form(...), url: str = Form(...),
              html_text: str = Form(...), gold_text: str = Form("")):
    error = success = None
    try:
        r1 = requests.post(f"{BACKEND_URL}/add_web_resource",
                           json={"url": url, "html_text": html_text}, timeout=120)
        ok1 = r1.status_code == 200 and r1.json().get("status") == "ok"
        if not ok1:
            error = "Errore nel salvataggio della web resource."
        else:
            r2 = requests.post(f"{BACKEND_URL}/add_gold_standard",
                               json={"url": url, "gold_text": gold_text}, timeout=120)
            if r2.status_code == 200 and r2.json().get("status") == "ok":
                success = "Entry salvata nel Gold Standard."
            else:
                error = "Errore nel salvataggio del gold_text."
    except requests.RequestException as exc:
        error = f"Errore di comunicazione con il backend: {exc}"

    return templates.TemplateResponse(request, "gold_standard.html",
                                      _gs_context(domain, error=error, success=success))


@app.post("/gold-standard/delete", response_class=HTMLResponse)
def gold_delete(request: Request, domain: str = Form(...), url: str = Form(...)):
    error = success = None
    try:
        r = requests.delete(f"{BACKEND_URL}/gold_standard", json={"url": url}, timeout=120)
        if r.status_code == 200 and r.json().get("status") == "ok":
            success = "Entry eliminata dal Gold Standard."
        else:
            error = "Errore nell'eliminazione."
    except requests.RequestException as exc:
        error = f"Errore di comunicazione con il backend: {exc}"

    return templates.TemplateResponse(request, "gold_standard.html",
                                      _gs_context(domain, error=error, success=success))


@app.get("/stats", response_class=HTMLResponse)
def stats_page(request: Request):
    data = {}
    error = None
    try:
        r = requests.get(f"{BACKEND_URL}/db_stats", timeout=120)
        if r.status_code == 200:
            data = r.json()
        else:
            error = f"Errore /db_stats ({r.status_code})"
    except requests.RequestException as exc:
        error = f"Errore di comunicazione con il backend: {exc}"

    web_resources = data.get("web_resources", {})
    domains = sorted(web_resources.keys())
    return templates.TemplateResponse(
        request,
        "stats.html",
        {
            "active": "stats",
            "domains": domains,
            "web_resources": web_resources,
            "gold_standard": data.get("gold_standard", {}),
            "avg_eval": data.get("avg_eval", {}),
            "avg_eval_judge": data.get("avg_eval_judge", {}),
            "avg_advanced": data.get("avg_advanced", {}),
            "error": error,
        },
    )


# --- Tesi (personalizzazione 4a): pagina "Valutazione avanzata" ---
# nel container il frontend gira come modulo "src.frontend" (vedi Dockerfile)
try:  # noqa: E402
    from src import advanced_routes
except ImportError:
    import advanced_routes

advanced_routes.setup(templates, BACKEND_URL, get_domains, get_all_gs_urls)
app.include_router(advanced_routes.router)
