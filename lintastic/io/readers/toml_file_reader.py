from typing import Any, Dict

import tomli

from lintastic.io.interfaces.file_reader import IFileReader


class TomlFileReader(IFileReader):
    @staticmethod
    def read(file_path: str) -> Dict[str, Any]:
        with open(file_path, 'rb') as file:
            return tomli.load(file)
