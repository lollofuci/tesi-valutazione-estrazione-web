"""LLM-as-Judge: valutazione qualitativa del parsing tramite un LLM locale (Ollama).

Invia parsed_text e gold_text al modello con un prompt strutturato che chiede un
JSON {score 1-5, feedback}; se il modello non rispetta il formato si usa un fallback.
"""

import json
import os
import re

import requests

from evaluation.evaluator import remove_markdown

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://ollama:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:1b")
MAX_CHARS = int(os.getenv("JUDGE_MAX_CHARS", "3000"))       # troncamento input (velocita' su CPU)
REQUEST_TIMEOUT = int(os.getenv("JUDGE_TIMEOUT", "120"))

PROMPT_TEMPLATE = """Valuta la qualità del seguente testo estratto da una pagina web.

Testo estratto dal parser:
{parsed_text}

Testo di riferimento (Gold Standard):
{gold_text}

Rispondi SOLO con un JSON nel seguente formato:
{{
  "score": <intero tra 1 e 5>,
  "feedback": "<breve descrizione della qualità del testo>"
}}"""


def _truncate(text: str, max_chars: int) -> str:
    if text and len(text) > max_chars:
        return text[:max_chars]
    return text or ""


def _build_prompt(parsed_text: str, gold_text: str) -> str:
    parsed_plain = _truncate(remove_markdown(parsed_text), MAX_CHARS)
    gold_plain = _truncate(remove_markdown(gold_text), MAX_CHARS)
    return PROMPT_TEMPLATE.format(parsed_text=parsed_plain, gold_text=gold_plain)


def _clamp_score(value) -> int | None:
    """Converte lo score in un intero nell'intervallo [1, 5]; None se non valido."""
    try:
        score = int(round(float(value)))
    except (TypeError, ValueError):
        return None
    return max(1, min(5, score))


def _parse_judge_output(raw: str) -> dict | None:
    """Estrae {score, feedback} dall'output; prova anche il primo blocco {...}."""
    if not raw:
        return None
    candidates = [raw]
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if match:
        candidates.append(match.group(0))
    for candidate in candidates:
        try:
            data = json.loads(candidate)
        except (json.JSONDecodeError, TypeError):
            continue
        if not isinstance(data, dict):
            continue
        score = _clamp_score(data.get("score"))
        if score is None:
            continue
        return {"score": score, "feedback": str(data.get("feedback", ""))}
    return None


def _fallback(feedback: str) -> dict:
    return {"model_name": OLLAMA_MODEL, "judge_score": 1, "judge_feedback": feedback}


def evaluate_judge(parsed_text: str, gold_text: str) -> dict:
    """Ritorna {model_name, judge_score, judge_feedback}."""
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": _build_prompt(parsed_text, gold_text),
        "stream": False,
        "format": "json",
        "options": {"temperature": 0},
    }
    try:
        response = requests.post(f"{OLLAMA_HOST}/api/generate", json=payload, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        raw_output = response.json().get("response", "")
    except requests.RequestException as exc:
        return _fallback(f"Modello non raggiungibile o errore di rete: {exc}")

    parsed = _parse_judge_output(raw_output)
    if parsed is None:
        return _fallback("Il modello non ha restituito un JSON valido nel formato atteso.")
    return {"model_name": OLLAMA_MODEL, "judge_score": parsed["score"], "judge_feedback": parsed["feedback"]}
