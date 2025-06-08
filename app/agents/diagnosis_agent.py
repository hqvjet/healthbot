import ollama

from app.utils import config
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

class DiagnosisAgent():
    def __init__(self):
        self.config = config['prompting']['diagnosis_agent']
        self.agent_name = self.config['name']
        example_formatter = PromptTemplate.from_template(
            "Question: {question}\nAnswer: {answer}"
        )
        self.fewshot_prompt = FewShotPromptTemplate(
            example_prompt=example_formatter,
            examples=self.config['examples'],
            suffix="Question: {question}\nAnswer:",
            input_variables=["question"]
        )

    def get_prompts(self):
        return self.fewshot_prompt