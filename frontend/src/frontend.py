import os
import requests

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8003")


def get_domains() -> list[str]:
    response = requests.get(f"{BACKEND_URL}/domains", timeout=60)
    response.raise_for_status()
    data = response.json()
    return data.get("domains", [])


def get_all_gs_urls() -> list[str]:
    urls: list[str] = []

    try:
        domains = get_domains()
    except Exception:
        return []

    for domain in domains:
        try:
            response = requests.get(
                f"{BACKEND_URL}/full_gold_standard",
                params={"domain": domain},
                timeout=120,
            )
            if response.status_code != 200:
                continue

            data = response.json()
            gold_standard_entries = data.get("gold_standard", [])

            for entry in gold_standard_entries:
                url = entry.get("url")
                if url:
                    urls.append(url)

        except Exception:
            continue

    return sorted(set(urls))


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    gs_urls = get_all_gs_urls()

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "request": request,
            "gs_urls": gs_urls,
        },
    )


@app.post("/parse", response_class=HTMLResponse)
def parse_url(request: Request, url: str = Form(...)):
    parse_data = None
    gold_data = None
    eval_data = None
    error = None

    try:
        parse_response = requests.get(
            f"{BACKEND_URL}/parse",
            params={"url": url},
            timeout=120,
        )

        if parse_response.status_code != 200:
            error = f"Errore in /parse: {parse_response.text}"
        else:
            parse_data = parse_response.json()

            gold_response = requests.get(
                f"{BACKEND_URL}/gold_standard",
                params={"url": url},
                timeout=120,
            )

            if gold_response.status_code == 200:
                gold_data = gold_response.json()

                eval_response = requests.post(
                    f"{BACKEND_URL}/evaluate",
                    json={
                        "parsed_text": parse_data["parsed_text"],
                        "gold_text": gold_data["gold_text"],
                    },
                    timeout=120,
                )

                if eval_response.status_code == 200:
                    eval_data = eval_response.json()

    except requests.RequestException as exc:
        error = f"Errore di comunicazione con il backend: {exc}"

    return templates.TemplateResponse(
        request,
        "result.html",
        {
            "request": request,
            "selected_url": url,
            "parse_data": parse_data,
            "gold_data": gold_data,
            "eval_data": eval_data,
            "error": error,
            "gs_urls": get_all_gs_urls(),
        },
    )