from src.parsers.models import ParseResult
from .models import InventoryClass, InventoryFunction, RepositoryInventory

class InventoryBuilder:
    def build(self, language, parse_results:list[ParseResult]):
        all_classes = []
        all_functions = []

        for result in parse_results:
            for cls in result.classes:
                all_classes.append(
                    InventoryClass(
                        file_path=result.file_path,
                        class_name=cls.name, 
                        methods=cls.methods
                    )
                )

            for func in result.functions:
                all_functions.append(
                    InventoryFunction(
                        file_path=result.file_path,
                        name=func.name,
                        parameters=func.parameters,
                        start_line=func.start_line,
                        end_line=func.end_line
                    )
                )

        return RepositoryInventory(
            language=language,
            total_files=len(parse_results),
            total_classes=len(all_classes),
            total_functions=len(all_functions),
            classes=all_classes,
            functions=all_functions
        )