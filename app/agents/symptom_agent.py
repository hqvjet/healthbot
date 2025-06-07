import ollama

class SymptomAgent:
    def __init__(self, model_name: str = "symptom-agent"):
        self.model_name = model_name
        self.client = ollama.Client()

    def get_symptoms(self, query: str) -> str:
        """
        Get symptoms based on the provided query.
        
        :param query: The query string to analyze.
        :return: A string containing the symptoms.
        """
        response = self.client.chat(
            model=self.model_name,
            messages=[{"role": "user", "content": query}]
        )
        return response['message']['content']