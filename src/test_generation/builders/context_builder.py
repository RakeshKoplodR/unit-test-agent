from src.test_generation.models import TestGenerationContext

class ContextBuilder:

    def build(
        self,
        language,
        framework,
        function
    ):
        return TestGenerationContext(
            language=language,
            framework=framework.test_framework,
            import_path=function.import_path,
            module_name=function.module_name,
            class_name=function.class_name,
            function_name=function.name,
            source_code=function.source_code,
            
        )