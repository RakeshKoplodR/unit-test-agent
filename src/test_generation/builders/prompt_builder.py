SYSTEM_PROMPT= """
You are a senior software engineer. Generate production ready unit tests.
Requirements:
1. Cover happy paths
2. Cover edge caases
3. Cover negative cases
4. Cover exceptions
5. Follow framework best practices
6. Do not explain anything

Return only executable test code.
"""

class PromptBuilder:
    def build_prompt(
        self,
        context
    ):
        # from src.string_ops  import String_Ops
        prompt = f"""
    Language: {context.language}
    Module: {context.module_name}
    Framework:{context.framework}
    Function: {context.function_name}
    Source Code: {context.source_code}
    IMPORTANT: The function belongs to module: {context.module_name}
    Use: from {context.import_path} import {context.class_name}
    when generating tests. Do not invent import paths. Do not use solution.py
    Generate complete executable unit tests.
    """
        return prompt
        

