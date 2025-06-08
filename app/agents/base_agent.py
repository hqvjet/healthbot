from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from utils import config

prompt_config = config['prompt']

class HealthBotAgents:

    def __init__(self, retriever):
        self.model = OllamaLLM(
            model=config['model']['name']
        )
        self.prompt = ChatPromptTemplate.from_template(prompt_config['template'])
        self.chain = self.prompt | self.model
        self.retriever = retriever

    def execute(self, query, msg_history):
        """
        Execute the agent with the given query.
        """
        # Retrieve relevant documents
        docs = self.retriever.invoke(query)

        # Generate the response using the model
        response = self.chain.stream({"conversation": docs, "question": query, "msg_history": msg_history})

        return response