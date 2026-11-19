LANGUAGE_DEFAULTS = {
    "Python": {
        "test_framework": "pytest",
        "mock_framework": "unittest.mock",
        "coverage_tool": "pytest-cov"
    },
    "java": {
        "test_framework": "junits",
        "mock_framework": "mockito",
        "coverage_tool": "jacoco"
    },
    "swift": {
        "test_framework": "xctest",
        "mock_framework": "xctest",
        "coverage_tool": "xccov"
    },
    "javascript": {
        "test_framework": "jest",
        "mock_framework": "jest.mock",
        "coverage_tool": "jest"
    },
    "typescript": {
        "test_framework": "jest",
        "mock_framework": "jest.mock",
        "coverage_tool": "jest"
    }
}