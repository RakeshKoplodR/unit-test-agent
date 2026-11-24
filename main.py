from pathlib import Path

from src.services.repair_service import RepairService
from src.parsers.parser_factory import ParserFactory
from src.repo_loader.loader import RepositoryLoader
from src.language_detector.language_detector import LanguageDetector
from src.services.code_inventory_service import CodeInventoryService
from src.services.framework_service import FrameworkService
from src.services.test_generation_service import TestGenerationService
from dotenv import load_dotenv
from src.services.validation_service import ValidateService

load_dotenv()

def main():

    print("\n========================================================")
    print("STEP 1 :- REPOSITORY LOADER")
    loader = RepositoryLoader()
    #https://github.com/RakeshKoplodR/demo_git_project
    #https://github.com/pallets/flask
    repo_info = loader.clone_repository(github_url="https://github.com/RakeshKoplodR/demo_git_project")
    print(repo_info.model_dump())

    
    print("\n========================================================")
    print("STEP 2 :- LANGUAGE DETECTION")
    detector = LanguageDetector()
    language_detector_result = detector.detectLanguage(
        repo_info.local_path
    )
    print(language_detector_result.model_dump())
    # parser = ParserFactory.get_parser(language_detector_result.primary_language)
    # for file in language_detector_result.source_files:
    #     result = parser.parse(file)
    #     print(result.model_dump())


    print("\n========================================================")
    print("STEP 3 :- REPOSITORY INVENTORY")
    service = CodeInventoryService()
    inventory = service.generate_inventory(
        language=language_detector_result.primary_language,
        source_files=language_detector_result.source_files,
        repo_root=repo_info.local_path
    )
    print(inventory.get_statistics())


    print("\n========================================================")
    print("STEP 4 :- FRAMEWORK MAPPING")
    framework_service = FrameworkService()
    framework = framework_service.detect_framework(
        repo_path=repo_info.local_path,
        language=inventory.language
    )
    print(framework.model_dump_json())


    print("\n========================================================")
    print("STEP 5 :- TEST GENERATION")
    test_service = TestGenerationService()
    test_service.generate_tests(
        inventory=inventory,
        framework=framework,
        repo_path=repo_info.local_path
    )


    print("\n========================================================")
    print("STEP 6 :- TEST VALIDATION")
    validation_service = ValidateService()
    validation_results = validation_service.validate(repo_path=repo_info.local_path)
    failed_result = None
    for result in validation_results:
        print(f"{result.test_file}")
        print(f"\n Success: {result.success}")
        if not result.success:
            failed_result = result
            print(result.failure_log)
            break

    if not failed_result:
        print("All generated tests passed.")
        return


    print("\n========================================================")    
    print("STEP 7 :- FAILED TEST REPAIR")
    repair_service = RepairService()
    function = inventory.functions[0]
    generated_test = Path(failed_result.test_file).read_text(encoding="utf-8")
    fixed_test = repair_service.repair_test(
        function=function,
        generated_test=generated_test,
        framework=framework,
        validation_result=failed_result
    )
    Path(failed_result.test_file).write_text(fixed_test, encoding="utf-8")


    print("\n========================================================")
    print("STEP 8 :- TEST RE-VALIDATION")
    re_validation = validation_service.validator.validate_test(
        repo_info.local_path,
        failed_result.test_file
    )
    print(re_validation.success)
    if not re_validation.success:
        print(f"Still failing with error: {re_validation.failure_log}")


if __name__=="__main__":
    main()