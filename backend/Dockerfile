FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    wget \
    ca-certificates \
    gcc \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

# PyTorch solo CPU (per BERTScore): evita di scaricare le librerie CUDA, inutili qui.
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m playwright install --with-deps chromium

COPY backend/src ./src
COPY gs_data ./gs_data
COPY domains.json .

EXPOSE 8003

# All'avvio: init del DB, poi avvio del server (da /app/src per gli import).
WORKDIR /app/src
CMD ["sh", "-c", "python -m db.init_db && uvicorn server:app --host 0.0.0.0 --port 8003"]