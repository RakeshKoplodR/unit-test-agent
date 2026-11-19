from pathlib import Path
from collections import Counter

from .constants import(
    BUILD_INDICATORS,
    EXTENSION_LANGUAGE_MAP
)

from .models import LamguageDetectionResult

class LanguageDetector:
    def detectLanguage(
            self, 
            repo_path:str
) -> LamguageDetectionResult:
        repo = Path(repo_path)
        language_counter = Counter()
        indicators = []
        source_files = []

        for file in repo.rglob("*"):
            if file.is_file():
                extension = file.suffix.lower()
                if extension in EXTENSION_LANGUAGE_MAP:
                    language = EXTENSION_LANGUAGE_MAP[extension]
                    language_counter[language] += 1
                    source_files.append(str(file))
                    #print(f"Source file ====> {str(file)}")
                if file.name in BUILD_INDICATORS:
                    indicators.append(file.name)
                    language_counter[BUILD_INDICATORS[file.name]]

        if not language_counter:
            return LamguageDetectionResult(
                primary_language="Unknown",
                confidence=0,
                extension_counts={},
                inidcators=[]
            )

        detected_language = max(
            language_counter,
            key=language_counter.get
        )

        total = sum(
            language_counter.values()
        )

        confidence = (
            language_counter[detected_language]/total
        ) * 100


        return LamguageDetectionResult(
            primary_language=detected_language,
            confidence=round(confidence, 2),
            extension_counts=dict(language_counter),
            inidcators=indicators,
            source_files=source_files
        )