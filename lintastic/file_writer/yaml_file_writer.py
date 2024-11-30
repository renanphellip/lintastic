import os
from typing import Any

import yaml


class YamlFileWriter:
    # ruff: noqa: PLR6301
    def write(self, output_path: str, data: Any) -> str:
        absolute_output_path = os.path.abspath(output_path.strip())
        with open(absolute_output_path, 'w', encoding='utf-8') as file:
            yaml.safe_dump(data, file, sort_keys=False, indent=2)
        return absolute_output_path
