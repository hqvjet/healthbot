from langchain_core.prompts import ChatPromptTemplate
from ollama import AsyncClient


class HealthBotAgents:

    def __init__(self):
        pass

    def get_prompt(self) -> ChatPromptTemplate:
        """
        Returns the prompt template for the agent.
        """
        return self.prompt_template

    def set_prompt(self, prompt: ChatPromptTemplate):
        """
        Sets the prompt template for the agent.
        """
        self.prompt_template = prompt

client = AsyncClient()