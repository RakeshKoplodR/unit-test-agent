from src.parsers.parser_factory import ParserFactory
from src.repo_loader.loader import RepositoryLoader
from src.language_detector.language_detector import LanguageDetector
from src.services.code_inventory_service import CodeInventoryService
from src.services.framework_service import FrameworkService

def main():

    loader = RepositoryLoader()

    #https://github.com/RakeshKoplodR/demo_git_project
    #https://github.com/pallets/flask
    
    repo_info = loader.clone_repository(github_url="https://github.com/RakeshKoplodR/demo_git_project")

    # print(repo_info.model_dump())

    detector = LanguageDetector()

    language_detector_result = detector.detectLanguage(
        repo_info.local_path
    )

    #print(language_detector_result.model_dump())

    # parser = ParserFactory.get_parser(language_detector_result.primary_language)
    # for file in language_detector_result.source_files:
    #     result = parser.parse(file)
    #     print(result.model_dump())

    service = CodeInventoryService()

    inventory = service.generate_inventory(
        language=language_detector_result.primary_language,
        source_files=language_detector_result.source_files
    )

    framework_service = FrameworkService()

    framework = framework_service.detect_framework(
        repo_path=repo_info.local_path,
        language=inventory.language
    )

    print(framework.model_dump_json())

    stats = inventory.get_statistics()
    print(stats)



if __name__=="__main__":
    main()