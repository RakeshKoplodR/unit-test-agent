SYSTEM_PROMPT = """
You are a senior software engineer. Abgenerated unit test has failed. Your task is to repair the test.
Rules:
1. Fix only the test.
2. Do not modify source code.
3. Use validation logs.
4. Produce executable code only.
5. Return full updated test file"""

class RepairPromptBuilder:
    def build(self, context):
        prompt = f"""
            Module: {context.failure_log}
            Framework:{context.generated_test}
            Function: {context.function_name}
            Source Code: {context.source_code}
            Repair the test.
            """
                
        return prompt