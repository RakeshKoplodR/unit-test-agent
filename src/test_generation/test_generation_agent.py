from src.test_generation.llm.openai_provider import ChatAIProvider
from src.test_generation.models import GeneratedTest
from src.test_generation.builders.prompt_builder import SYSTEM_PROMPT



class TestGenerationAgent:
    def __init__(self):
        self.model = ChatAIProvider.get_llm()

    def generate_test(
            self,
            prompt
    ):

        response = self.model.invoke(
            [
                ("system", SYSTEM_PROMPT),
                ("human", prompt)
            ]
        )

        # Track token usage
        usage = response.response_metadata.get(
            "token_usage", {}
        )

        prompt_details = usage.get(
            "prompt_tokens_details", {}
        )

        print("Input tokens:",
              usage.get("prompt_tokens", 0))

        print("Output tokens:",
              usage.get("completion_tokens", 0))

        print("Cached tokens:",
              prompt_details.get("cached_tokens", 0))

        return response.content