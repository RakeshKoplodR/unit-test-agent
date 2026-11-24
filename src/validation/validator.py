from src.validation.test_runner import PyTestRunner
from src.validation.models import ValidateTestResult

class TestValidator:
    def __init__(self):
        self.runner = (PyTestRunner())

    def validate_test(
        self,
        repo_path,
        test_file
    ):
        execution = self.runner.execute(
            repo_path,
            test_file
        )

        return ValidateTestResult(
            success=execution.returncode == 0,
            test_file=test_file,
            exit_code=execution.returncode,
            stdout=execution.stdout,
            stderr=execution.stderr,
            error_type=execution.stderr
        )