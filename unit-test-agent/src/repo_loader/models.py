from pydantic import BaseModel

class RepositoryInfo(BaseModel):
    github_url: str
    repo_name: str
    local_path: str
    is_exisiting_repo: bool