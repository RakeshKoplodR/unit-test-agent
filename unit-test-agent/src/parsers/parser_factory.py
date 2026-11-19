from .python_parser import PythonParser

class ParserFactory:

    @staticmethod
    def get_parser(language: str):
        if language == "Python":
            return PythonParser()

        raise ValueError("Unsupported language")