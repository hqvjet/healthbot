# Import necessary modules
from langchain_core.prompts import ChatPromptTemplate  # For creating chat-based prompt templates
from langchain_google_genai import ChatGoogleGenerativeAI  # For interacting with Google Generative AI



from app.utils import prompts  # Import custom prompts from the utils module

class IntentClassifier:
    """
    A class for classifying user intents using Google Generative AI.

    Attributes:
        chain: A chain combining a prompt templates and a generative AI model.
    """

    def __init__(self, model: ChatGoogleGenerativeAI):
        """
        Initialize the IntentClassifier with a generative AI model and a prompt template.

        Args:
            model: An optional generative AI model
        """
        prompt = ChatPromptTemplate.from_template(prompts['intent_template'])
        self.chain = prompt | model

    def invoke(self, query: str) -> str:
        """
        Invoke the intent classification chain with a user query.

        Args:
            query: The user query string to classify.

        Returns:
            A list of classified intents as strings.
        """
        intents = self.chain.invoke({"question": query, "fewshot": prompts['intent_fewshot']}).content
        intents = intents.strip().replace(' ', '')
        intents = intents.split(',')
        return intents