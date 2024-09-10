import sys

from rich.console import Console

from lintastic.file_reader.file_reader import IFileReader
from lintastic.file_reader.json_file_reader import JsonFileReader
from lintastic.file_reader.toml_file_reader import TomlFileReader
from lintastic.file_reader.yaml_file_reader import YamlFileReader


class FileReaderFactory:
    @staticmethod
    def get_file_reader(file_path: str) -> IFileReader:
        file_path = file_path.lower()
        if file_path.endswith('.toml'):
            return TomlFileReader()
        elif file_path.endswith('.json'):
            return JsonFileReader()
        elif file_path.endswith(('yaml', 'yml')):
            return YamlFileReader()
        else:
            console = Console(highlight=False)
            console.print(
                f'[red]Unsupported file extension: {file_path}[/red]'
            )
            sys.exit(1)
