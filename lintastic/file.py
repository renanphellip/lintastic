import json
import os
import sys
from typing import Any, Dict

import tomli
import yaml
from rich.console import Console

console = Console(highlight=False)


def read_file(file_path: str, verbose=False) -> Dict[str, Any]:
    try:
        absolute_file_path = os.path.abspath(file_path.strip())
        if verbose:
            console.print(
                'The absolute file path is: '
                f'[blue]{absolute_file_path}[/blue]'
            )
            console.print(f'Loading "[blue]{absolute_file_path}[/blue]"...')
        if absolute_file_path.endswith('.toml'):
            with open(absolute_file_path, 'rb') as file:
                return tomli.load(file)
        elif absolute_file_path.endswith('.json'):
            with open(absolute_file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            with open(absolute_file_path, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
    except Exception as error:
        console.print(
            f'[red]Failed to read the file "{absolute_file_path}": '
            f'{error}[/red]'
        )
        sys.exit(1)
