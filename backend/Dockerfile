FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m playwright install --with-deps chromium

COPY backend/src ./src
COPY gs_data ./gs_data
COPY domains.json .

EXPOSE 8003

CMD ["uvicorn", "server:app", "--app-dir", "/app/src", "--host", "0.0.0.0", "--port", "8003"]