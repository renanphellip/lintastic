from typing import Any, Dict

import yaml

from lintastic.io.interfaces.file_reader import IFileReader


class YamlFileReader(IFileReader):
    @staticmethod
    def read(file_path: str) -> Dict[str, Any]:
        with open(file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
