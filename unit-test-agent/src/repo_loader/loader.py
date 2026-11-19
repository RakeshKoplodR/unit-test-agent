import logging 
import shutil
from pathlib import Path

from git import Repo
from git.exc import GitCommandError

from .models import RepositoryInfo
from .exceptions import (
    InvalidGitHubUrlException,
    CloneRepositoryException
)

from .constants import WORKSPACE_DIR

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class RepositoryLoader:
    def __init__(self):
        WORKSPACE_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

    def validate_url(self, github_url: str):
        if not github_url.startswith("https://github.com"):
            raise InvalidGitHubUrlException(f"Invalid GitHub URL: {github_url}")

    def extract_repo_name(self, github_url: str) -> str:
        repo_name = github_url.rstrip("/").split("/")[-1]
        repo_name = repo_name.replace(".git", "")
        return repo_name

    def clone_repository(self, github_url: str, shallow_clone: bool = True) -> RepositoryInfo:
        self.validate_url(github_url)
        repo_name = self.extract_repo_name(github_url)
        repo_path = WORKSPACE_DIR / repo_name
        logging.info(f"Repository path: {repo_path}")
        print(f"Repository path: {repo_path}")

        if repo_path.exists():
            logging.info("Removing existing repository")
            print("Removing existing repository")
            print(f"Repository path: {repo_path}")
            shutil.rmtree(repo_path)
        
        if shallow_clone:
            try:
                Repo.clone_from(github_url, str(repo_path), depth=1)
                print("Clone completed successfully")
                return RepositoryInfo(
                    github_url=github_url,
                    repo_name=repo_name,
                    local_path=str(repo_path),
                    is_exisiting_repo=False
                )
            except GitCommandError as exception:
                raise CloneRepositoryException(
                    f"Clone failed: {str(exception)}"
                ) from exception

        
