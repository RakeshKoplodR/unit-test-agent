# import subprocess


# class PyTestRunner:
#     def execute(
#         self,
#         repo_path,
#         test_file
#     ):

#         result = subprocess.run(["pytest", test_file, "-v"],cwd=repo_path, capture_output=True, text=True)
#         return result


import os
import sys
import subprocess


class PyTestRunner:

    def execute(self, repo_path, test_file):

        env = os.environ.copy()

        # Prioritize the target repository's source directory
        existing_pythonpath = env.get("PYTHONPATH", "")

        env["PYTHONPATH"] = (
            repo_path
            + os.pathsep
            + existing_pythonpath
        )

        command = [
            sys.executable,
            "-m",
            "pytest",
            test_file,
            "-v"
        ]

        result = subprocess.run(
            command,
            cwd=repo_path,
            env=env,
            capture_output=True,
            text=True
        )

        return result
