from pathlib import Path
from tree_sitter import Parser, Language
import tree_sitter_python
#from tree_sitter_python import language
from .models import (
    FunctionInfo,
    ClassInfo,
    ParseResult
)
from .base_parser import BaseParser

class PythonParser(BaseParser):
    def __init__(self):
        PY_LANGUAGE = Language(tree_sitter_python.language())
        self.parser = Parser(PY_LANGUAGE)

    def parse(self, file_path):
        source = Path(file_path).read_text(encoding="utf-8")
        tree = self.parser.parse(
            bytes(
                source,
                "utf-8"
            )
        )

        root = tree.root_node
        #print(f"Root ===> {source}")
        return ParseResult(
            file_path=file_path,
            functions=self.extract_functions(root, source=source),
            classes=self.extract_classes(root)
        )


    def print_tree(
            self,
            node,
            indent=""
    ):
       # print(f"{indent}{node.type}")
        for child in node.children:
            self.print_tree(
                child,
                indent + " "
            )

    def extract_functions(
            self,
            node,
            source
    ):
        functions = []

        if node.type == ("function_definition"):
            name_node = node.child_by_field_name("name")
            if name_node:
                function_source = source[node.start_byte: node.end_byte]
                functions.append(
                    FunctionInfo(
                        name=name_node.text.decode(),
                        parameters=[],
                        source_code=function_source,
                        start_line=node.start_point[0],
                        end_line=node.end_point[0]
                    )
                )

        for child in node.children:
            functions.extend(
                self.extract_functions(
                    child,
                    source
                )
            )

        return functions


    def extract_classes(
            self,
            node
    ):
        classes = []
        
        if node.type == ("class_definition"):
            name = node.child_by_field_name("name")
            methods = []
            body = node.child_by_field_name("body")

            if body:
                for child in node.children:
                    if node.type == ("function_definition"):
                        method_name = (child.child_by_field_name("name").text.decode())
                        methods.append(method_name)

            classes.append(
                ClassInfo(
                    name=name.text.decode(),
                    methods=methods
                )
            )

        for child in node.children:
            classes.extend(self.extract_classes(child))

        return classes