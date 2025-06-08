from langchain_ollama import OllamaLLM
from langchain_core.prompts import FewShotPromptTemplate

from app.utils import config

class HealthBotAgents:

    def __init__(self):
        self.model = OllamaLLM(
            model=config['model']['name']
        )

        self.diag_chain = None

    def set_prompt(self, prompt: FewShotPromptTemplate):
        """
        Sets the prompt template for the agent.
        """
        self.diag_chain = prompt | self.model

    def get_chain(self):
        """
        Returns the chain for the agent.
        """
        if self.diag_chain is None:
            raise ValueError("Prompt template not set. Please set the prompt using set_prompt method.")
        return self.diag_chain