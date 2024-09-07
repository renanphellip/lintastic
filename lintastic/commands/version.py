import sys
from typing import Literal

from rich import print

from lintastic.file.file_service import FileService


def version() -> Literal[True]:
    try:
        file_service = FileService()
        data = file_service.read_file('pyproject.toml')
        version = data['tool']['poetry']['version']
        if not version:
            raise KeyError
        print(f'\nLintastic CLI version: {version}\n')
        return True
    except Exception:
        print('\n[red]Lintastic version was not specified.[/red]\n')
        sys.exit(1)
