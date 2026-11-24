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

    def parse(self, file_path, repo_root):
        source = Path(file_path).read_text(encoding="utf-8")
        tree = self.parser.parse(
            bytes(
                source,
                "utf-8"
            )
        )

        root = tree.root_node
        class_name = ""
       
        #print(f"Root ===> {source}")
        
        return ParseResult(
            file_path=file_path,
            functions=self.extract_functions(root, source=source, file_path=file_path, current_class_name=class_name, repo_root=repo_root),
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
            source,
            file_path,
            repo_root,
            current_class_name
    ):
        functions = []

        if node.type == "class_definition":
            name_node = node.child_by_field_name("name")
            if name_node:
                current_class_name = name_node.text.decode("utf-8")

        if node.type == ("function_definition"):
            name_node = node.child_by_field_name("name")
            if name_node:
                function_source = source[node.start_byte: node.end_byte]
                module_name = Path(file_path).stem
                import_path = self.build_import_path(file_path, repo_root)
                parameters = []
                parameters_node = node.child_by_field_name("parameters")
                if parameters_node:
                    for child in parameters_node.children:
                        if child.type == "typed_parameter":
                            parameters.append(child.text.decode())
                functions.append(
                    FunctionInfo(
                        file_path=file_path,
                        module_name=module_name,
                        class_name=current_class_name,
                        name=name_node.text.decode(),
                        parameters=parameters,
                        import_path=import_path,
                        source_code=function_source,
                        start_line=node.start_point[0],
                        end_line=node.end_point[0]
                    )
                )

        for child in node.children:
            functions.extend(
                self.extract_functions(
                    node=child,
                    source=source,
                    file_path=file_path,
                    current_class_name= current_class_name if node.type == "class_definition"
                    else current_class_name,
                    repo_root=repo_root
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

    def build_import_path(self, file_path: str,repo_root: str):
        relative = Path(file_path).relative_to(repo_root)
        import_path = str(relative).replace("\\", ".").replace("/", ".").replace(".py", "")
        return import_path