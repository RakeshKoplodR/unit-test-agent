from pathlib import Path

from src.validation.validator import TestValidator

class ValidateService:
    def __init__(self):
        self.validator = TestValidator()

    def validate(
        self,
        repo_path
    ):
        generated_path = Path(repo_path)/"generated_tests"
        results = []
        for file in generated_path.glob("test_*.py"):
            result = self.validator.validate_test(
                repo_path,
                str(file)
            )
            results.append(result)

        return results