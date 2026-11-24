from pydantic import BaseModel

class RepairContext(BaseModel):
    
    function_name: str

    source_code: str

    generated_test: str

    failure_log: str

    framework: str