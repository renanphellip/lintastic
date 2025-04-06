from typing import Any, Dict

import tomli


class TomlFileReader:
    # ruff: noqa: PLR6301
    def read(self, file_path: str) -> Dict[str, Any]:
        with open(file_path, 'rb') as file:
            return tomli.load(file)
