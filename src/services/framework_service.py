from src.framework_mapper.framework_mapper import FrameworkMapper

class FrameworkService:
    def detect_framework(self, repo_path, language):
        mapper = FrameworkMapper()
        return mapper.detect(
            language=language,
            repo_path=repo_path
        )