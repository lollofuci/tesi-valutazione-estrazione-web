"""Valutazione avanzata dei parser (personalizzazione 4a della tesi).

Moduli:
- text_utils:    normalizzazione, tokenizzazione, riconoscimento lingua, testo visibile da HTML
- metrics:       metriche lessicali (token F1, ROUGE-L, chrF, METEOR)
- bertscore:     metrica semantica BERTScore con gestione dei testi lunghi
- judges:        LLM-as-Judge generalizzato (piu' modelli, con e senza Gold Standard)
- perturbations: degradazioni controllate del testo per la meta-valutazione
- agreement:     correlazioni e accordo tra metriche e giudici
"""
