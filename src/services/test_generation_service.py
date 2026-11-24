from src.test_generation.selectors.function_selector import FunctionSelector
from src.test_generation.builders.context_builder import ContextBuilder
from src.test_generation.builders.prompt_builder import PromptBuilder
from src.test_generation.test_generation_agent import TestGenerationAgent
from src.test_generation.utils.generated_test_writer import GeneratedTestWriter

class TestGenerationService:
    
    def __init__(self):
        self.selector = FunctionSelector()
        self.context_builder = ContextBuilder()
        self.prompt_builder = PromptBuilder()
        self.agent = TestGenerationAgent()
        self.writer = GeneratedTestWriter()

    def generate_tests(
            self,
            inventory,
            framework,
            repo_path
    ):
        #generated_tests = []

        functions = self.selector.select_functions(inventory)
        for function in functions[:1]:
            context = self.context_builder.build(
                inventory.language,
                framework,
                function
            )

            prompt = self.prompt_builder.build_prompt(context=context)

            generated_test = self.agent.generate_test(prompt=prompt)

            self.writer.save(
                repo_path,
                function.file_path,
                generated_test
            )
