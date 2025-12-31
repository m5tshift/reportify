import os
from typing import List
from pprint import pprint


def scan_repo(repo_path: str, extensions: List[str]) -> List[str]:
    result = []

    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [dir for dir in dirs if not dir.startswith(".") and "venv" not in dir]

        for file in files:
            if any(file.endswith(extention) for extention in extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        result.append(f"*{file}*\n```python\n{content}\n```\n")
                except Exception as e:
                    print(f"Skipping file: {file}. Error: {e}")
    return result


if __name__ == "__main__":
    pprint(scan_repo(".", ["py"]))
