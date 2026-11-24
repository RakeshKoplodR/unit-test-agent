from pydantic import BaseModel

class GeneratedTest(BaseModel):
    file_name: str
    framework: str
    function_name: str
    test_code: str
    generation_status: str

class TestGenerationContext(BaseModel):
    language: str
    framework: str
    module_name: str
    class_name: str | None
    import_path: str
    function_name: str
    source_code: str
