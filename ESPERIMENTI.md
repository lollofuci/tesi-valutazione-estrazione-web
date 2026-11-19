# Esperimenti della tesi – Valutazione avanzata dei parser

Personalizzazione **4a** del progetto di Laboratorio di Ingegneria Informatica.

## Cosa c'è di nuovo nel codice

| Percorso | Contenuto |
|---|---|
| `backend/src/evaluation/advanced/metrics.py` | Token F1 (metrica base), ROUGE-L, chrF, METEOR |
| `backend/src/evaluation/advanced/bertscore.py` | BERTScore per testi lunghi (a blocchi da 510 token) |
| `backend/src/evaluation/advanced/judges.py` | LLM-as-Judge con qualsiasi modello Ollama, con e senza Gold Standard |
| `backend/src/evaluation/advanced/perturbations.py` | Degradazioni controllate del Gold Standard |
| `backend/src/evaluation/advanced/agreement.py` | Correlazioni (Spearman, Kendall) e kappa pesata |
| `backend/src/experiments/` | Script degli esperimenti e dell'analisi |
| `esperimenti.sh` | Comandi per lanciare tutto da terminale |
| `results/` | Risultati, tabelle LaTeX e grafici (creata dagli script) |

## Preparazione (una volta sola)

1. Installa **Ollama per Mac** da https://ollama.com/download e aprilo (icona del lama nella barra in alto).
2. Scarica i modelli giudice, uno alla volta:
   ```
   ollama pull llama3.2:1b
   ollama pull llama3.2:3b
   ollama pull phi4-mini
   ollama pull qwen3:4b
   ```
   (Erano previsti anche `gemma4:e2b` e `ministral-3:3b`, esclusi per limiti di memoria e di spazio su disco.)
3. Dalla cartella principale del repository:
   ```
   chmod +x esperimenti.sh
   ./esperimenti.sh build
   ```

## Esecuzione

```
./esperimenti.sh casi        # pochi minuti
./esperimenti.sh metriche    # qualche decina di minuti (BERTScore scarica il modello la prima volta)
caffeinate -i ./esperimenti.sh giudici    # molte ore: caffeinate impedisce al Mac di andare in stop
./esperimenti.sh analisi
```

Tutti gli script si possono interrompere (Ctrl+C) e rilanciare: ripartono da dove erano rimasti.
Per provare un solo modello: `./esperimenti.sh giudici --models qwen3:4b --limit 5`.
Per vedere quante valutazioni mancano senza lanciarle: `./esperimenti.sh giudici --dry-run`.

## Disegno sperimentale

- **Dati**: i 20 documenti del Gold Standard (5 per dominio), con l'HTML "congelato".
- **Casi** (340): per ogni documento l'output reale del parser, il Gold Standard intatto e
  15 varianti degradate (5 tipi × gravità 0,25 / 0,5 / 0,75):
  troncamento, righe eliminate, boilerplate aggiunto (preso dall'HTML della pagina),
  ordine alterato, numeri alterati.
- **Metriche**: calcolate su tutti i 340 casi.
- **Giudici**: 4 modelli × 2 modalità (con GS / senza GS, cioè testo visibile della pagina + testo estratto)
  su 140 casi (output dei parser, GS intatto, perturbazioni a gravità 0,5): 1 120 giudizi.
- **Analisi**:
  - qualità dei parser secondo ogni metrica;
  - sensibilità di ogni metrica e giudice alla gravità dell'errore;
  - accordo tra metriche e giudici;
  - accordo tra il giudizio con GS e quello senza GS.

## La pagina "Valutazione avanzata" nella Web UI

La personalizzazione è integrata nel sistema:

- **Backend** (`backend/src/advanced_api.py`), nuovi endpoint REST:
  - `POST /advanced_evaluate`: tutte le metriche tra testo estratto e Gold Standard (BERTScore facoltativo);
  - `GET /judge_models`: modelli disponibili per il giudice;
  - `POST /advanced_judge`: giudice LLM a scelta, con o senza Gold Standard;
  - `GET /full_gs_advanced_eval?domain=…`: metriche avanzate su tutto il GS di un dominio, salvate nel DB;
  - `GET /experiment_results` e `GET /experiment_figure/{nome}`: risultati e grafici degli esperimenti.
- **`POST /evaluate`**: il campo `x_eval` ora contiene gli F-score di ROUGE-L, chrF e METEOR.
- **Database**: nuova tabella `advanced_evaluations`. `/db_stats` restituisce anche le medie avanzate.
- **Frontend**:
  - nuova pagina `/advanced` ("Valutazione avanzata");
  - la pagina Stats mostra anche ROUGE-L, chrF, METEOR e BERTScore.

Avvio:
```
docker compose up --build
```
Poi apri http://localhost:8004/advanced.

Note sull'avvio:
- I giudici avanzati usano l'Ollama installato sul Mac, se è aperto. Altrimenti usano il container `ollama`, che ha solo `llama3.2:1b`.
- Il container `ollama` del progetto ora espone la porta **11435**, così non entra in conflitto con quello del Mac (11434).
