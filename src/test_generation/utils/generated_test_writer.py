from pathlib import Path

class GeneratedTestWriter:

    def save(
        self,
        repo_path,
        source_file,
        test_code
    ):
        source = Path(source_file)
        output = Path(repo_path)/"generated_tests"/f"test_{source.stem}.py"
        output.parent.mkdir(
            parents=True,
            exist_ok=True
        )
        output.write_text(
            test_code,
            encoding="utf-8"
        )