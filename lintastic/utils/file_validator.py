import os
import sys
from typing import Literal, Tuple
from rich.console import Console

class FileValidator:
    def __init__(self, console=Console()):
        self.console = console

    def validate_extension(self, file_path: str, supported_extensions: Tuple[str], verbose=False) -> Literal[True]:
        if not file_path.lower().endswith(supported_extensions):
            self.console.print(f'[red]The file path "{file_path}" does not have a valid extension: {supported_extensions}[/red]')
            sys.exit(1)
        if verbose:
            self.console.print(f'The "[blue]{file_path}[/blue]" file has a valid extension.')
        return True

    def validate_existence(self, file_path: str, verbose=False) -> Literal[True]:
        if not os.path.exists(file_path):
            self.console.print(f'[red]The file path "{file_path}" was not found.[/red]')
            sys.exit(1)
        if verbose:
            self.console.print(f'The "[blue]{file_path}[/blue]" file path exists as expected.')
        return True
