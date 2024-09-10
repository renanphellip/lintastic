import json
import os
from dataclasses import asdict
from typing import Any

from lintastic.entities.validator import ValidationResultCollection


class JsonFileWriter:
    def write(output_path: str, data: Any) -> str:
        absolute_output_path = os.path.abspath(output_path.strip())
        with open(absolute_output_path, 'w', encoding='utf-8') as file:
            if isinstance(data, ValidationResultCollection):
                json.dump(asdict(data), file, sort_keys=False, indent=2)
            else:
                json.dump(data, file, sort_keys=False, indent=2)
        return absolute_output_path
