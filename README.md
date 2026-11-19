# Valutazione della qualità dell'estrazione di contenuti web

Codice della tesi di laurea triennale in Ingegneria Informatica e Automatica (Sapienza Università di Roma, a.a. 2025/2026):

> **Valutazione della qualità dell'estrazione di contenuti web: metriche automatiche e LLM-as-Judge a confronto**
> Lorenzo Augusto Fucito — relatore Prof. Roberto Navigli

Il sistema estrae il contenuto principale di pagine web di quattro domini (Wikipedia, ATP Tour, AccuWeather, Trading Economics) con parser specifici per dominio e ne valuta la qualità rispetto a un Gold Standard scritto a mano. La tesi estende la valutazione con nuove metriche e con giudici LLM di dimensioni diverse, e li confronta su casi di test di qualità nota.

## Autori

- **Progetto base** (Laboratorio di Ingegneria Informatica): Lorenzo Augusto Fucito, Emiliano Frioni, Matteo Mercieri — parser, Gold Standard, metrica `token_level_eval`, giudice LLM, database, API REST, interfaccia web, Docker.
- **Personalizzazione 4a, valutazione avanzata dei parser** (tesi): Lorenzo Augusto Fucito — metriche ROUGE-L, chrF, METEOR e BERTScore, giudici LLM con e senza Gold Standard, perturbazioni controllate, esperimenti, pagina "Valutazione avanzata".

## Architettura

Quattro servizi orchestrati da Docker Compose:

| Servizio | Tecnologia | Porta |
|---|---|---|
| `backend` | FastAPI: parser, metriche, giudici, API REST | 8003 |
| `frontend` | FastAPI + Jinja2: interfaccia web | 8004 |
| `mariadb` | MariaDB 11: pagine, Gold Standard, valutazioni | 3306 |
| `ollama` | Ollama con `llama3.2:1b`, il giudice del progetto | 11435 |

I giudici della valutazione avanzata usano l'Ollama installato sul computer (porta 11434), se è in esecuzione; altrimenti il container `ollama`.

## Struttura del repository

```
backend/src/
  parsers/                 parser per dominio (classe base BaseParser)
  evaluation/evaluator.py  token_level_eval (metrica del progetto)
  evaluation/judge.py      giudice LLM del progetto
  evaluation/advanced/     valutazione avanzata (tesi)
    text_utils.py          normalizzazione, token, lingua, testo visibile della pagina
    metrics.py             Token F1, ROUGE-L (LCS bit-parallela), chrF, METEOR
    bertscore.py           BERTScore per documenti lunghi (blocchi da 510 token)
    judges.py              giudici LLM con qualsiasi modello Ollama, con e senza Gold Standard
    perturbations.py       degradazioni controllate del Gold Standard
    agreement.py           correlazioni e kappa di Cohen pesata
  experiments/             script degli esperimenti e dell'analisi
  db/                      schema, connessione e accesso a MariaDB
  server.py                API REST del progetto
  advanced_api.py          API REST della valutazione avanzata
  test_metrics.py          test delle metriche rispetto alle implementazioni di riferimento
frontend/                  interfaccia web (template Jinja2)
gs_data/                   Gold Standard: 5 pagine per dominio, con HTML salvato
results/                   risultati degli esperimenti, tabelle LaTeX e grafici
esperimenti.sh             comandi per rieseguire gli esperimenti
ESPERIMENTI.md             guida agli esperimenti
```

## Avvio

Serve Docker Desktop. Dalla cartella principale:

```bash
docker compose up --build
```

Al primo avvio vengono scaricati il modello del giudice e le dipendenze, e vengono precalcolate le valutazioni del Gold Standard: può richiedere alcuni minuti. Poi:

- interfaccia web: http://localhost:8004
- valutazione avanzata: http://localhost:8004/advanced
- documentazione interattiva delle API: http://localhost:8003/docs

Per spegnere: `docker compose down`.

Per usare i giudici più grandi, installare [Ollama](https://ollama.com) sul computer e scaricare i modelli:

```bash
ollama pull llama3.2:3b
ollama pull phi4-mini
ollama pull qwen3:4b
```

## Test delle metriche

Le metriche reimplementate sono verificate rispetto a implementazioni indipendenti (programmazione dinamica per la LCS, sacrebleu per chrF, NLTK per METEOR):

```bash
pip install -r backend/requirements.txt pytest sacrebleu
cd backend/src
python -m pytest test_metrics.py -v
```

## Esperimenti

I risultati della tesi sono già in `results/`. Per rieseguire gli esperimenti (340 casi di test, 1 120 giudizi) si veda [ESPERIMENTI.md](ESPERIMENTI.md).

Risultati principali:

- `token_level_eval` è cieca all'ordine del testo (sensibilità 0,09), che ROUGE-L invece rileva (0,92);
- il giudice del progetto (`llama3.2:1b`) non distingue un'estrazione corretta da una degradata;
- i giudici da 3–4 miliardi di parametri migliorano (phi4-mini: 0,46), ma sugli stessi casi restano meno sensibili di tutte le metriche;
- senza Gold Standard nessun giudice è affidabile.

## Note

Le credenziali del database in `docker-compose.yaml` sono valori predefiniti per l'uso in locale.
