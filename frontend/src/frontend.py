import os
import requests

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8003")


def get_domains() -> list[str]:
    try:
        response = requests.get(f"{BACKEND_URL}/domains", timeout=60)
        response.raise_for_status()
        data = response.json()
        return data.get("domains", [])
    except Exception:
        return []


def get_all_gs_urls() -> list[str]:
    urls: list[str] = []
    domains = get_domains()

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
        # verifichiamo se l'URL è nel Gold Standard
        gold_response = requests.get(
            f"{BACKEND_URL}/gold_standard",
            params={"url": url},
            timeout=120,
        )

        if gold_response.status_code == 200:
            # L'URL è nel Gold Standard 
            # Estraiamo l'HTML salvato e usiamo la POST per il parsing offline
            gold_data = gold_response.json()
            html_text = gold_data.get("html_text", "")
            
            parse_response = requests.post(
                f"{BACKEND_URL}/parse",
                json={
                    "url": url,
                    "html_text": html_text
                },
                timeout=120,
            )
        else:
            #L'URL non è nel Gold Standard (è un URL nuovo inserito a mano).
            #Andiamo live su internet con la GET
            parse_response = requests.get(
                f"{BACKEND_URL}/parse",
                params={"url": url},
                timeout=120,
            )

        #Gestiamo il risultato del parsing (sia esso live o offline)
        if parse_response.status_code != 200:
            error = f"Errore nel parsing: {parse_response.text}"
        else:
            parse_data = parse_response.json()

            #Se avevamo i dati del Gold Standard, calcoliamo le metriche
            if gold_data:
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