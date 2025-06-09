# Import necessary modules
from duckduckgo_search import DDGS  # For performing image searches using DuckDuckGo
from langchain_core.prompts import ChatPromptTemplate  # For creating chat-based prompt templates

from app.utils import prompts  # Import configuration settings

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
        self.search_engine = DDGS()
        prompt = ChatPromptTemplate.from_template(prompts['keyword_extract_template'])
        self.chain = prompt | model

    def search_img(self, query: str):
        """
        Search for images related to the given query using DuckDuckGo.

        Args:
            query: The search query string.

        Returns:
            A list of image search results.
        """
        print('GOOOOOOOOOOOOOOOOOOOOOOOO')
        results = DDGS().images(keywords=query, max_results=3)
        return results

    def execute(self, query: str):
        """
        Execute the image search agent with the given query.

        Args:
            query: The user query string.

        Returns:
            A list of image search results or None if no images are found.
        """
        print(query)
        query = self.chain.invoke({"question": query, "fewshot": prompts['keyword_extract_fewshot']}).content
        results = self.search_img(query)
        if results:
            return results
        else:
            print("No images found for the given query.")
            return None