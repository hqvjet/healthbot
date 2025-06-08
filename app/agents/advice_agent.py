import ollama
# from app.agents.base_agent import BaseAgent

# class DiagnosisAgent(BaseAgent):
#     def __init__(self, model_name: str = "diagnosis-agent"):
#         super().__init__(name="Diagnosis Agent", description="Agent for diagnosing conditions based on symptoms.")
#         self.model_name = model_name
#         self.client = ollama.Client()

#     def diagnose(self, query: str) -> str:
#         """
#         Diagnose a condition based on the provided query.
        
#         :param query: The query string to analyze.
#         :return: A string containing the diagnosis.
#         """
#         response = self.client.chat(
#             model=self.model_name,
#             messages=[{"role": "user", "content": query}]
#         )
#         return response['message']['content']