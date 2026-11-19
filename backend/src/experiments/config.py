"""Parametri comuni agli esperimenti (modificabili anche da variabili d'ambiente)."""

from __future__ import annotations

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent      # .../backend o /app nel container
GS_DIR = Path(os.getenv("GS_DIR", BASE_DIR / "gs_data"))
RESULTS_DIR = Path(os.getenv("RESULTS_DIR", BASE_DIR / "results"))

CASES_PATH = RESULTS_DIR / "cases.jsonl"
PARSED_PATH = RESULTS_DIR / "parsed_outputs.json"
METRICS_PATH = RESULTS_DIR / "metrics.jsonl"
JUDGES_PATH = RESULTS_DIR / "judges.jsonl"
TABLES_DIR = RESULTS_DIR / "tables"
FIGURES_DIR = RESULTS_DIR / "figures"

# Perturbazioni: tipi e livelli di gravita'
SEVERITIES = [0.25, 0.5, 0.75]

# Giudici: il modello del progetto base + modelli consigliati nelle slide del corso.
# Esclusi: ministral-3:3b (spazio su disco) e gemma4:e2b (richiede 6,9 GB di RAM libera,
# non disponibili su un MacBook Air da 8 GB).
JUDGE_MODELS = [
    "llama3.2:1b",
    "llama3.2:3b",
    "phi4-mini",
    "qwen3:4b",
]
JUDGE_MODES = ["with_gs", "without_gs"]

# Sottoinsieme di casi su cui far girare i giudici (piu' lenti delle metriche):
# output reali dei parser + GS intatto + ogni perturbazione alla severity indicata.
JUDGE_SEVERITY = 0.5

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://ollama:11434")
JUDGE_MAX_CHARS = int(os.getenv("JUDGE_MAX_CHARS", "6000"))
JUDGE_NUM_CTX = int(os.getenv("JUDGE_NUM_CTX", "12288"))
