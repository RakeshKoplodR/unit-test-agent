from pydantic import BaseModel

class FunctionInfo(BaseModel):
    name: str
    parameters: list[str]
    source_code: str
    start_line: int
    end_line: int

class ClassInfo(BaseModel):
    name: str
    methods: list[str]

class ParseResult(BaseModel):
    file_path: str
    functions: list[FunctionInfo]
    classes: list[ClassInfo]