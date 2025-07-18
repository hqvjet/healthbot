# Import necessary modules
from langchain_google_genai import ChatGoogleGenerativeAI  # For interacting with Google Generative AI
from dotenv import load_dotenv  # For loading environment variables from a .env file
import os  # For accessing environment variables

import app.agents as agents  # Import agent classes
from app.data.vector import load_retriever  # Import retriever for document search

# Load environment variables from the .env file
load_dotenv()

class Orchestrator:
    """
    A class for orchestrating various agents to handle user queries.

    Attributes:
        retriever: A retriever for fetching relevant documents.
        intent_classifier: An agent for classifying user intents.
        advise_agent: An agent for providing health advice.
        disease_image_search_agent: An agent for searching disease-related images.
    """

    def __init__(self):
        """
        Initialize the Orchestrator with necessary agents and components.
        """
        self.retriever = load_retriever()
        model = ChatGoogleGenerativeAI(
            model='gemma-3-27b-it', temperature=0.1, max_output_tokens=1000,
            google_api_key=os.getenv('AI_STUDIO_API_KEY'),
        )
        self.intent_classifier = agents.IntentClassifier(model=model)
        self.advise_agent = agents.AdviseAgent(model=model, retriever=self.retriever)
        self.disease_image_search_agent = agents.DiseaseImageSearchAgent(model=model)

    def classify_intent(self, query: str, msg_history: list):
        """
        Classify the intent of a user query.

        Args:
            query: The user query string.

        Returns:
            A list of classified intents.
        """
        intents = self.intent_classifier.invoke(query, msg_history)
        return intents

    def get_advice(self, query: str, msg_history: list):
        """
        Get health advice based on the user query and message history.

        Args:
            query: The user query string.
            msg_history: The history of messages exchanged in the conversation.

        Returns:
            A streamming response generated by the AdviseAgent. The response needs to be handled to be used.
        """
        response = self.advise_agent.execute(query, msg_history)
        return response

    def get_image_search_results(self, query: str):
        """
        Get disease-related image search results based on the user query.

        Args:
            query: The user query string.

        Returns:
            A list of image search results or None if no images are found.
        """
        results = self.disease_image_search_agent.execute(query)
        return results