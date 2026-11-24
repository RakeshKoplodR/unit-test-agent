from pydantic import BaseModel, Field

class InventoryFunction(BaseModel):
    file_path: str
    module_name: str
    class_name: str | None = None
    import_path: str
    name: str
    parameters: list[str]
    source_code: str
    start_line: int
    end_line: int

class InventoryClass(BaseModel):
    file_path: str
    class_name: str
    methods: list[str]

class RepositoryInventory(BaseModel):
    language: str
    total_files: int
    total_classes: int
    total_functions: int
    classes: list[InventoryClass] = Field(default_factory=list)
    functions: list[InventoryFunction] = Field(default_factory=list)

    def get_class(self, class_name: str):
        for cls in self.classes:
            if cls.class_name == class_name:
                return cls
        return None

    def get_function(self, functions_name: str):
        for function in self.functions:
            if function.name == functions_name:
                return function
        return None

    def get_statistics(self):
        avg_functions_per_file = 0
        if self.total_files > 0:
            avg_functions_per_file = (self.total_functions / self.total_files)

        return {
            "language":self.language,
            "total_files": self.total_files,
            "total_classes": self.total_classes,
            "total_functions": self.total_functions,
            "avg_functions_per_file": round(avg_functions_per_file, 2),
        }