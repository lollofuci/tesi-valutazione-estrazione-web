"""Esperimenti della tesi: valutazione avanzata dei parser.

Ordine di esecuzione (dalla cartella backend/src, dentro il container backend):
    python -m experiments.build_cases     # parsing offline del GS + varianti perturbate
    python -m experiments.run_metrics     # metriche lessicali e BERTScore
    python -m experiments.run_judges      # LLM-as-Judge (con e senza Gold Standard)
    python -m experiments.analyze         # tabelle LaTeX e grafici per la tesi
"""
