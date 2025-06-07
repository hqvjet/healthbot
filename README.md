# Health Diagnosis Chatbot

A conversational AI chatbot that helps users with preliminary health diagnosis and medical advice using advanced language models.

## Overview

This chatbot leverages multiple specialized agents to provide a comprehensive health consultation experience:
- Symptom Analysis
- Medical Diagnosis
- Health Advice

## Features

- Interactive chat interface using Chainlit
- Multi-agent architecture for specialized health-related tasks
- Real-time symptom analysis and diagnosis suggestions
- Medical advice based on user inputs
- Error handling and graceful session management

## Prerequisites

- Python 3.12.1
- Ollama
- Required Python packages (listed in requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd healthbot
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

To start the chatbot, run:
```bash
chainlit run ui/app.py
```

The chatbot will be available at `http://localhost:8000` by default.

## Project Structure

```
├── app/
│   ├── agents/           # Specialized AI agents
│   │   ├── advice_agent.py
│   │   ├── diagnosis_agent.py
│   │   └── symptom_agent.py
│   ├── chains/          # Language model chains
│   │   └── health_chain.py
│   └── config.yaml      # Configuration settings
├── ui/
│   └── app.py          # Main application interface
├── data/               # Data resources
└── tests/              # Test suite
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

None

## Disclaimer

This chatbot is for informational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.