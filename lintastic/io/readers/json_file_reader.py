import json
from typing import Any, Dict

from lintastic.io.interfaces.file_reader import IFileReader


class JsonFileReader(IFileReader):
    @staticmethod
    def read(file_path: str) -> Dict[str, Any]:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
