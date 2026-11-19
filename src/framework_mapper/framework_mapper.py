from pathlib import Path
from .constants import LANGUAGE_DEFAULTS
from .models import FrameworkResult

class FrameworkMapper:

    def detect_pytest(self, repo_path):
        repo = Path(repo_path)
        for file in repo.rglob("*.py"):
            try:
                content = file.read_text(encoding="utf-8")
                if "import pytest" in content:
                    return True
            except:
                pass
        return False

    def detect(self, language, repo_path):
        if(language == "Python" and self.detect_pytest(repo_path=repo_path)):
            return FrameworkResult(
                language=language,
                test_framework="pytest",
                mock_framework="unittest.mock",
                coverage_tool="pytest-cov",
                test_directory="tests",
                confidence=100,
                detection_reason=("Existing pytest imports found")
            )
        defaults = LANGUAGE_DEFAULTS[language]

        return FrameworkResult(
            language=language,
            test_framework=defaults["test_framework"],
            mock_framework=defaults["mock_framework"],
            coverage_tool=defaults["coverage_tool"],
            test_directory="tests",
            confidence=80,
            detection_reason=("Language default")
        )
