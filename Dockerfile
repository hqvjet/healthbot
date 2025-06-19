FROM python:3.12.1-slim

WORKDIR /app
ENV PYTHONPATH=/app

# Install necessary system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       curl \
       build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

CMD ollama serve > /tmp/ollama.log 2>&1 & \
    pid=$!; \
    for i in $(seq 1 10); do \
      ollama ls >/dev/null 2>&1 && break; \
      sleep 1; \
    done; \
    ollama pull bge-m3; \
    kill $pid; \
    exec ollama serve & \
    exec chainlit run ui/main.py --host 0.0.0.0 --port 8000