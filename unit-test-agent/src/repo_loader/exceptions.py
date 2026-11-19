class RepositoryLoaderException(Exception):
    """Base repository exception"""
    def __init__(self, message="An error occurred while loading the repository"):
        super().__init__(message)

class InvalidGitHubUrlException(RepositoryLoaderException):
    """Raise when git hub url is invalid"""
    def __init__(self, message="Invalid GitHub repository URL"):
        super().__init__(message)

class CloneRepositoryException(RepositoryLoaderException):
    """Raise when repository clone fails"""
    def __init__(self, message="Failed to clone the GitHub repository"):
        super().__init__(message)
