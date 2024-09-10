import os
import sys
from typing import Any

from rich.console import Console

from lintastic.file_writer.file_writer_factory import FileWriterFactory


class FileWriterService:
    def __init__(self, console=Console()):
        self.console = console

    def write_file(self, output_path: str, data: Any, verbose=False) -> str:
        try:
            self.__create_output_directory(output_path, verbose)
            absolute_output_path = os.path.abspath(output_path.strip())
            if verbose:
                self.console.print(
                    'The absolute output path is: '
                    f'[blue]{absolute_output_path}[/blue]'
                )
                self.console.print(
                    f'Creating "[blue]{absolute_output_path}[/blue]"...'
                )
            file_writer = FileWriterFactory.get_file_writer(
                absolute_output_path
            )
            absolute_output_path = file_writer.write(output_path, data)
            return absolute_output_path
        except Exception as error:
            self.console.print(
                f'[red]Failed to write the file "{absolute_output_path}": '
                f'{error}[/red]'
            )
            sys.exit(1)

    def __create_output_directory(
        self, output_path: str, verbose: bool
    ) -> None:
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            if verbose:
                self.console.print(
                    f'The path "[blue]{output_dir}[/blue]" not exists. '
                    'Creating...'
                )
            os.makedirs(output_dir)
