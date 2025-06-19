# HealthBot

HealthBot is a conversational assistant that offers preliminary health advice and disease-related image search. It showcases a multi-agent design powered by Chainlit and Google Generative AI.

## Features

- **Intent classification** to detect whether a user needs advice, images or both.
- **Health advice agent** that retrieves relevant documents from a vector database built with the `hungnm/vietnamese-medical-qa` dataset.
- **Image search agent** using Google Custom Search to fetch medical illustrations.
- **Chainlit interface** with OAuth and password authentication examples.
- **Dockerfile** for easy deployment with Ollama and the `bge-m3` embedding model.

## Requirements

- Python 3.12+
- [Ollama](https://ollama.com) installed locally
- Packages from `requirements.txt`

## Quick Start

1. Clone the repository and install dependencies:
   ```bash
   git clone <repository-url>
   cd healthbot
   pip install -r requirements.txt
   ```
2. Copy environment variables template and edit it with your keys:
   ```bash
   cp .env_example .env
   ```
3. (Optional) Build the vector store:
   ```bash
   python app/data/create_vectordb.py
   ```
4. Launch the chatbot:
   ```bash
   chainlit run ui/main.py
   ```
   The UI will be available at `http://localhost:8000`.

## Project Structure

```
├── app/
│   ├── agents/              # AI agents and orchestrator
│   ├── data/                # Vector store utilities
│   └── utils.py             # Config and prompt loaders
├── ui/
│   └── main.py              # Chainlit entrypoint
├── Dockerfile               # Container configuration
└── requirements.txt         # Python dependencies
```

## Environment Variables

The application relies on several variables (see `.env_example`):

- `AI_STUDIO_API_KEY`
- `GOOGLE_CUSTOM_SEARCH_API_KEY`
- `SEARCH_ENGINE_ID`
- `CHAINLIT_AUTH_SECRET`
- `OAUTH_GOOGLE_CLIENT_ID`
- `OAUTH_GOOGLE_CLIENT_SECRET`
- `DATABASE_URL`

## License

None

## Disclaimer

HealthBot is intended for informational purposes only and should not be used as a substitute for professional medical advice, diagnosis or treatment. Always seek the guidance of a qualified healthcare provider with any questions regarding a medical condition.
