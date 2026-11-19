"""LLM-as-Judge generalizzato.

Rispetto al giudice del progetto base (evaluation/judge.py) permette di:
- scegliere il modello Ollama (per confrontare giudici di dimensioni diverse);
- giudicare CON Gold Standard (testo estratto vs testo di riferimento) oppure
  SENZA Gold Standard (testo estratto vs testo visibile dell'HTML grezzo);
- fissare esplicitamente la finestra di contesto (num_ctx): il valore predefinito di
  Ollama (2048 token) puo' troncare in silenzio il prompt;
- registrare, oltre al punteggio, validita' del JSON, latenza e risposta grezza.
"""

from __future__ import annotations

import json
import os
import re
import time
from dataclasses import asdict, dataclass

import requests

from evaluation.advanced.text_utils import html_visible_text, normalize_text, truncate_chars

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://ollama:11434")

# Rubrica comune: stessi livelli di punteggio per entrambe le modalita'.
RUBRIC = """Scala di punteggio:
5 = contenuto principale completo, nessun elemento estraneo
4 = quasi completo, poche omissioni o poco rumore
3 = parti importanti mancanti oppure rumore evidente (menu, pubblicita', footer)
2 = gran parte del contenuto mancante o sommerso dal rumore
1 = testo inutilizzabile o non pertinente"""

PROMPT_WITH_GS = """Sei un valutatore della qualita' dell'estrazione di testo da pagine web.
Confronta il TESTO ESTRATTO dal parser con il TESTO DI RIFERIMENTO (Gold Standard), che
contiene esattamente il contenuto informativo corretto della pagina.
Valuta completezza (manca qualcosa del riferimento?), pulizia (ci sono menu, pubblicita',
banner o testo ripetuto?) e correttezza (testo alterato, numeri sbagliati, ordine confuso?).

{rubric}

TESTO ESTRATTO:
<<<
{parsed}
>>>

TESTO DI RIFERIMENTO:
<<<
{reference}
>>>

Rispondi SOLO con un JSON: {{"score": <intero da 1 a 5>, "feedback": "<una o due frasi>"}}"""

PROMPT_WITHOUT_GS = """Sei un valutatore della qualita' dell'estrazione di testo da pagine web.
Ti viene dato il TESTO DELLA PAGINA (tutto il testo visibile, compresi menu, pubblicita',
footer e altri elementi di contorno) e il TESTO ESTRATTO da un parser, che dovrebbe
contenere SOLO il contenuto informativo principale (titolo e corpo).
Valuta se il testo estratto contiene il contenuto principale della pagina, se esclude gli
elementi di contorno e se e' fedele alla pagina (nessun testo inventato o alterato).

{rubric}

TESTO DELLA PAGINA:
<<<
{reference}
>>>

TESTO ESTRATTO:
<<<
{parsed}
>>>

Rispondi SOLO con un JSON: {{"score": <intero da 1 a 5>, "feedback": "<una o due frasi>"}}"""

# Modelli "a ragionamento": va disattivato il pensiero esplicito, che allunga di molto
# i tempi e puo' far uscire testo fuori dal JSON.
THINKING_PREFIXES = ("qwen3", "deepseek-r1", "gpt-oss", "magistral")

# Tetto alla lunghezza della risposta: senza, qwen3 a volte genera migliaia di token.
MAX_OUTPUT_TOKENS = 512


@dataclass
class JudgeResult:
    model: str
    mode: str                  # "with_gs" | "without_gs"
    score: int | None          # None se il modello non ha restituito un JSON valido
    feedback: str
    valid_json: bool
    latency_s: float
    prompt_chars: int
    prompt_tokens: int | None   # token del prompt effettivamente elaborati da Ollama
    output_tokens: int | None
    raw: str
    error: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


def parse_judge_output(raw: str) -> tuple[int | None, str]:
    """Estrae (score, feedback) dalla risposta; prova anche il primo blocco {...}."""
    if not raw:
        return None, ""
    candidates = [raw]
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if match:
        candidates.append(match.group(0))
    for candidate in candidates:
        try:
            data = json.loads(candidate)
        except (json.JSONDecodeError, TypeError):
            continue
        if not isinstance(data, dict) or "score" not in data:
            continue
        try:
            score = int(round(float(data["score"])))
        except (TypeError, ValueError):
            continue
        if 1 <= score <= 5:
            return score, str(data.get("feedback", ""))
    return None, ""


class OllamaJudge:
    def __init__(self, model: str, host: str = OLLAMA_HOST, max_chars: int = 6000,
                 num_ctx: int = 12288, timeout: int = 900, temperature: float = 0.0) -> None:
        self.model = model
        self.host = host.rstrip("/")
        self.max_chars = max_chars
        self.num_ctx = num_ctx
        self.timeout = timeout
        self.temperature = temperature

    # -- costruzione dei prompt -------------------------------------------------
    def build_prompt(self, mode: str, parsed_text: str, gold_text: str = "", html: str = "") -> str:
        parsed = truncate_chars(normalize_text(parsed_text), self.max_chars)
        if mode == "with_gs":
            reference = truncate_chars(normalize_text(gold_text), self.max_chars)
            template = PROMPT_WITH_GS
        elif mode == "without_gs":
            # la pagina intera e' molto piu' lunga: le si concede il doppio dello spazio
            reference = truncate_chars(html_visible_text(html), 2 * self.max_chars)
            template = PROMPT_WITHOUT_GS
        else:
            raise ValueError(f"Modalita' sconosciuta: {mode}")
        return template.format(rubric=RUBRIC, parsed=parsed, reference=reference)

    # -- chiamata al modello ----------------------------------------------------
    def _generate(self, prompt: str) -> dict:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "format": "json",
            "options": {"temperature": self.temperature, "num_ctx": self.num_ctx, "seed": 42,
                        "num_predict": MAX_OUTPUT_TOKENS},
        }
        if self.model.startswith(THINKING_PREFIXES):
            payload["think"] = False
        response = requests.post(f"{self.host}/api/generate", json=payload, timeout=self.timeout)
        if response.status_code >= 400:
            # il messaggio di Ollama spiega la causa (es. memoria insufficiente)
            raise requests.HTTPError(f"HTTP {response.status_code}: {response.text[:300]}")
        return response.json()

    def judge(self, mode: str, parsed_text: str, gold_text: str = "", html: str = "") -> JudgeResult:
        prompt = self.build_prompt(mode, parsed_text, gold_text, html)
        start = time.perf_counter()
        data: dict = {}
        try:
            data = self._generate(prompt)
            error = ""
        except (requests.RequestException, ValueError) as exc:
            error = str(exc)
        raw = data.get("response", "")
        latency = time.perf_counter() - start
        score, feedback = parse_judge_output(raw)
        return JudgeResult(
            model=self.model, mode=mode, score=score, feedback=feedback,
            valid_json=score is not None, latency_s=round(latency, 3),
            prompt_chars=len(prompt), prompt_tokens=data.get("prompt_eval_count"),
            output_tokens=data.get("eval_count"), raw=raw[:2000], error=error,
        )

    def is_available(self) -> bool:
        """True se Ollama risponde e il modello e' gia' scaricato."""
        try:
            tags = requests.get(f"{self.host}/api/tags", timeout=10).json()
        except (requests.RequestException, ValueError):
            return False
        names = {m.get("name", "") for m in tags.get("models", [])}
        return self.model in names or f"{self.model}:latest" in names
