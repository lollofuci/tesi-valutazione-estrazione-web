"""Pagina "Valutazione avanzata" della Web UI (tesi, personalizzazione 4a).

Come il resto del frontend, comunica solo con le API REST del backend.
"""

import requests
from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, Response

router = APIRouter()

METRIC_LABELS = {
    "token": "Token F1 (progetto base)",
    "rougeL": "ROUGE-L",
    "chrf": "chrF",
    "meteor": "METEOR",
    "bertscore": "BERTScore",
}


# Dipendenze fornite dal frontend principale con setup() (evita import circolari).
_cfg: dict = {}


def setup(templates, backend_url: str, get_domains, get_all_gs_urls) -> None:
    _cfg.update(templates=templates, backend_url=backend_url,
                get_domains=get_domains, get_all_gs_urls=get_all_gs_urls)


def _get_json(path: str, timeout: int = 60, **params):
    try:
        r = requests.get(f"{_cfg['backend_url']}{path}", params=params, timeout=timeout)
        if r.status_code == 200:
            return r.json()
    except requests.RequestException:
        pass
    return None


def _detail(response) -> str:
    try:
        return response.json().get("detail", response.text)
    except ValueError:
        return response.text


def _base_context(**extra) -> dict:
    models = _get_json("/judge_models") or {}
    ctx = {
        "active": "advanced",
        "gs_urls": _cfg["get_all_gs_urls"](),
        "domains": _cfg["get_domains"](),
        "judge_models": models.get("models", []),
        "judge_host": models.get("host", ""),
        "experiments": _get_json("/experiment_results"),
        "metric_labels": METRIC_LABELS,
    }
    ctx.update(extra)
    return ctx


@router.get("/advanced", response_class=HTMLResponse)
def advanced_page(request: Request):
    return _cfg["templates"].TemplateResponse(request, "advanced.html", _base_context())


@router.post("/advanced/document", response_class=HTMLResponse)
def advanced_document(request: Request, url: str = Form(...), judge_model: str = Form(""),
                      judge_mode: str = Form("with_gs"), bertscore: str = Form("")):
    ctx = _base_context(selected_url=url, selected_model=judge_model,
                        selected_mode=judge_mode, bertscore=bool(bertscore))
    backend = _cfg['backend_url']
    try:
        # parsing offline (HTML salvato nel DB) e Gold Standard
        r = requests.post(f"{backend}/parse", json={"url": url, "local": True}, timeout=180)
        if r.status_code != 200:
            ctx["error"] = f"Errore nel parsing ({r.status_code}): {_detail(r)}"
            return _cfg["templates"].TemplateResponse(request, "advanced.html", ctx)
        parsed_text = r.json()["parsed_text"]
        g = requests.get(f"{backend}/gold_standard", params={"url": url}, timeout=60)
        if g.status_code != 200:
            ctx["error"] = "URL non presente nel Gold Standard."
            return _cfg["templates"].TemplateResponse(request, "advanced.html", ctx)
        gold_text = g.json()["gold_text"]
        ctx.update(parsed_text=parsed_text, gold_text=gold_text)

        ev = requests.post(f"{backend}/advanced_evaluate",
                           json={"parsed_text": parsed_text, "gold_text": gold_text,
                                 "bertscore": bool(bertscore)},
                           timeout=900)
        if ev.status_code == 200:
            ctx["doc_metrics"] = ev.json()["metrics"]
            ctx["doc_language"] = ev.json().get("language", "")
        else:
            ctx["error"] = f"Errore nelle metriche ({ev.status_code}): {_detail(ev)}"

        if judge_model:
            jd = requests.post(f"{backend}/advanced_judge",
                               json={"parsed_text": parsed_text, "gold_text": gold_text,
                                     "url": url, "model": judge_model, "mode": judge_mode},
                               timeout=900)
            if jd.status_code == 200:
                ctx["judge_result"] = jd.json()
            else:
                ctx["error"] = f"Errore del giudice ({jd.status_code}): {_detail(jd)}"
    except requests.RequestException as exc:
        ctx["error"] = f"Errore di comunicazione con il backend: {exc}"
    return _cfg["templates"].TemplateResponse(request, "advanced.html", ctx)


@router.post("/advanced/domain", response_class=HTMLResponse)
def advanced_domain(request: Request, domain: str = Form(...), bertscore: str = Form("")):
    ctx = _base_context(selected_domain=domain)
    try:
        r = requests.get(f"{_cfg['backend_url']}/full_gs_advanced_eval",
                         params={"domain": domain, "bertscore": bool(bertscore)}, timeout=1800)
        if r.status_code == 200:
            result = r.json()
            ctx["domain_result"] = result
            ctx["domain_columns"] = list(result.get("average", {}).keys())
        else:
            ctx["error"] = f"Errore nella valutazione del dominio ({r.status_code}): {_detail(r)}"
    except requests.RequestException as exc:
        ctx["error"] = f"Errore di comunicazione con il backend: {exc}"
    return _cfg["templates"].TemplateResponse(request, "advanced.html", ctx)


@router.get("/advanced/figure/{name}")
def advanced_figure(name: str):
    """Inoltra al browser i grafici degli esperimenti, che stanno nel backend."""
    try:
        r = requests.get(f"{_cfg['backend_url']}/experiment_figure/{name}", timeout=60)
        if r.status_code == 200:
            return Response(content=r.content, media_type="image/png")
    except requests.RequestException:
        pass
    return Response(status_code=404)
