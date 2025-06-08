FROM python:3.12.1-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       curl \
       build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | sh

RUN ollama serve
RUN ollama pull mrjacktung/phogpt-4b-chat-gguf
RUN ollama pull bge-m3

WORKDIR /app
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["chainlit", "run", "ui/main.py"]