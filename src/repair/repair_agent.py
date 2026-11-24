from src.test_generation.llm.openai_provider import ChatAIProvider
from src.repair.repair_prompt_builder import SYSTEM_PROMPT

class RepaiAgent:

    def __init__(self):
        self.model = ChatAIProvider.get_llm()
        
    def repair_test(self, prompt):
        response = self.model.invoke(
            [
                ("System", SYSTEM_PROMPT),
                ("human", prompt)
            ]
        )
        return response.content
