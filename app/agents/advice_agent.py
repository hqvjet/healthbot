# Import necessary modules
from langchain_ollama import OllamaLLM  # For interacting with Ollama language models
from langchain_core.prompts import ChatPromptTemplate  # For creating chat-based prompt templates

from app.utils import prompts  # Import configuration settings

class AdviseAgent:
    """
    A class for providing health advice based on user queries, retrieved documents and their conversation history.

    Attributes:
        chain: A chain combining a prompt template and a language model.
        retriever: A retriever for fetching relevant documents.
    """

    def __init__(self, model=None, retriever=None):
        """
        Initialize the AdviseAgent with a language model and a retriever.

        Args:
            model: An optional language model. If not provided, a default model can be used.
            retriever: An optional retriever for fetching relevant documents.
        """
        prompt = ChatPromptTemplate.from_template(prompts['advise_template'])
        self.chain = prompt | model
        self.retriever = retriever

    def execute(self, query, msg_history):
        """
        Execute the agent with the given query and conversation history.

        Args:
            query: The user query string.
            msg_history: The history of messages exchanged in the conversation.

        Returns:
            A streamming response by the language model based on the query and retrieved documents, 
            the reponse need to be handle to be used.
        """
        # Retrieve relevant documents
        docs = self.retriever.invoke(query)

        # Generate the response using the model
        response = self.chain.stream({"conversation": docs, "question": query, "msg_history": msg_history, "fewshot": prompts['advise_fewshot']})

        return response