from src.parsers.models import ParseResult
from src.parsers.parser_factory import ParserFactory
from src.inventory.inventory_builder import InventoryBuilder

class CodeInventoryService:

    def generate_inventory(self, language, source_files, repo_root):

        parser = ParserFactory.get_parser(language=language)
        parse_results = []

        for file in source_files:
            try:
                result = parser.parse(file, repo_root)
                parse_results.append(result)
            except Exception as exception:
                print(f"Failed ====> {file}")
                print(f"Exception =====> {exception}")

        inventory = (
            InventoryBuilder()
            .build(
                language=language,
                parse_results=parse_results
            )
        )

        return inventory