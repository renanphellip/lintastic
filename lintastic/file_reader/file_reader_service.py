import os
import sys
from typing import Any, Dict

from rich.console import Console

from lintastic.file_reader.file_reader_factory import FileReaderFactory


class FileReaderService:
    def __init__(self, console = Console(highlight=False)):
        self.console = console

    def read_file(self, file_path: str, verbose = False) -> Dict[str, Any]:
        absolute_file_path = os.path.abspath(file_path.strip())
        if verbose:
            self.console.print(
                f'Reading: [blue]{absolute_file_path}[/blue]'
            )
        try:
            file_reader = FileReaderFactory.get_file_reader(absolute_file_path)
            return file_reader.read(absolute_file_path)
        except Exception as error:
            self.console.print(
                f'[red]Failed to read: {absolute_file_path}\n'
                f'{error}[/red]'
            )
            sys.exit(1)
