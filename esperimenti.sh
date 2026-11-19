#!/bin/bash
# Esegue gli esperimenti della tesi dentro il container del backend.
# I giudici usano Ollama installato direttamente sul Mac (molto piu' veloce che in Docker,
# perche' sfrutta la GPU del chip Apple).
#
# Uso:
#   ./esperimenti.sh build              # ricostruisce l'immagine del backend (la prima volta)
#   ./esperimenti.sh casi               # parsing offline del GS + varianti perturbate
#   ./esperimenti.sh metriche           # metriche lessicali + BERTScore
#   ./esperimenti.sh giudici [opzioni]  # giudici LLM (es. --models qwen3:4b --modes with_gs)
#   ./esperimenti.sh analisi            # tabelle e grafici in results/
#   ./esperimenti.sh tutto              # casi + metriche + giudici + analisi

set -e
cd "$(dirname "$0")"
mkdir -p results

OLLAMA_HOST_MAC="${OLLAMA_HOST_MAC:-http://host.docker.internal:11434}"

run() {
  # il codice viene montato dalla cartella: le modifiche valgono subito, senza rifare la build
  docker compose run --rm --no-deps -e OLLAMA_HOST="$OLLAMA_HOST_MAC" \
    -v "$PWD/backend/src:/app/src" backend python -m "$@"
}

case "$1" in
  build)    docker compose build backend ;;
  casi)     run experiments.build_cases ;;
  metriche) run experiments.run_metrics ;;
  giudici)  shift; run experiments.run_judges "$@" ;;
  analisi)  run experiments.analyze ;;
  tutto)
    run experiments.build_cases
    run experiments.run_metrics
    run experiments.run_judges
    run experiments.analyze
    ;;
  *)
    sed -n '2,13p' "$0"
    exit 1
    ;;
esac
