from typing import Any, Dict

import yaml


class YamlFileReader:
    # ruff: noqa: PLR6301
    def read(self, file_path: str) -> Dict[str, Any]:
        with open(file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
