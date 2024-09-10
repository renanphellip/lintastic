import sys
from typing import Literal

from rich import print

from lintastic.file_reader.file_reader_service import FileReaderService


def version() -> Literal[True]:
    try:
        file_reader_service = FileReaderService()
        data = file_reader_service.read_file('pyproject.toml')
        version = data['tool']['poetry']['version']
        if not version:
            raise KeyError
        print(f'\nLintastic CLI version: {version}\n')
        return True
    except Exception:
        print('\n[red]Lintastic version was not specified.[/red]\n')
        sys.exit(1)
