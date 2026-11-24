from pydantic import BaseModel

class ValidateTestResult(BaseModel):
    success: bool
    test_file: str
    exit_code: int
    stdout: str
    stderr: str
    error_type: str