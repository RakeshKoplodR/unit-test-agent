from pydantic import BaseModel

class LamguageDetectionResult(BaseModel):
    primary_language: str
    confidence: float
    extension_counts: dict
    inidcators: list[str]
    source_files: list[str]