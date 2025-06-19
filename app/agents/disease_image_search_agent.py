# Import necessary modules
from langchain_core.prompts import ChatPromptTemplate  # For creating chat-based prompt templates
import os
from dotenv import load_dotenv  # For loading environment variables from a .env file
import requests  # For making HTTP requests to external APIs

from app.utils import prompts  # Import configuration settings


load_dotenv()

class DiseaseImageSearchAgent:
    """
    A class for searching disease-related images based on user queries.

    Attributes:
        search_engine: An instance of DuckDuckGo Search for image retrieval.
        chain: A chain combining a prompt template and a language model.
    """

    def __init__(self, model=None):
        """
        Initialize the DiseaseImageSearchAgent with a search engine and a language model.

        Args:
            model: An optional language model. If not provided, a default model can be used.
        """
        self.url = "https://www.googleapis.com/customsearch/v1"
        prompt = ChatPromptTemplate.from_template(prompts['keyword_extract_template'])
        self.chain = prompt | model

    def search_img(self, query: str, **params):
        """
        Search for images related to the given query using DuckDuckGo.

        Args:
            query: The search query string.

        Returns:
            A list of image search results.
        """
        params = {
            "key": os.getenv('GOOGLE_CUSTOM_SEARCH_API_KEY'),  # API key for Google Custom Search
            "cx": os.getenv('SEARCH_ENGINE_ID'),  # Custom Search Engine ID
            "q": query,
            "searchType": "image",  # Specify that we want image search results
            "num": 2,
            **params
        }
        res = requests.get(self.url, params=params)
        res.raise_for_status()
        res = res.json()
        res = res['items']
        return res

    def execute(self, query: str):
        """
        Execute the image search agent with the given query.

        Args:
            query: The user query string.

        Returns:
            A list of image search results or None if no images are found.
        """
        query = self.chain.invoke({"question": query, "fewshot": prompts['keyword_extract_fewshot']}).content
        results = self.search_img(query)
        if results:
            return results
        else:
            print("No images found for the given query.")
            return None