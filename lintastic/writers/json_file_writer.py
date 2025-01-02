import json
import os
from dataclasses import asdict
from typing import Any

from lintastic.entities.diagnostic import DiagnosticCollection


class JsonFileWriter:
    # ruff: noqa: PLR6301
    def write(self, output_path: str, data: Any) -> str:
        absolute_output_path = os.path.abspath(output_path.strip())
        with open(absolute_output_path, 'w', encoding='utf-8') as file:
            if isinstance(data, DiagnosticCollection):
                json.dump(asdict(data), file, sort_keys=False, indent=2)
            else:
                json.dump(data, file, sort_keys=False, indent=2)
        return absolute_output_path
