from src.repair.models import RepairContext
from src.repair.repair_prompt_builder import RepairPromptBuilder
from src.repair.repair_agent import RepaiAgent

class RepairService:

    def __init__(self):
        self.builder = RepairPromptBuilder()
        self.agent = RepaiAgent()

    def repair_test(
            self,
            function,
            generated_test,
            framework,
            validation_result
        ):
        context = RepairContext(
            function_name=function.name,
            source_code=function.source_code,
            generated_test=generated_test,
            framework=framework,
            failure_log=validation_result.failure_log
        )

        prompt = self.builder.build(context=context)

        return self.agent.repair_test(prompt)