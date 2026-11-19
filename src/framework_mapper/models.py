from pydantic import BaseModel

class FrameworkResult(BaseModel):
    language: str
    test_framework: str
    mock_framework: str
    coverage_tool: str
    test_directory: str
    confidence: float
    detection_reason: str
    