import sys
from typing import Literal

from rich import print

from lintastic.file import read_file


def version() -> Literal[True]:
    try:
        data = read_file('pyproject.toml')
        version = data['tool']['poetry']['version']
        print(f'\nLintastic CLI version: {version}\n')
        return True
    except KeyError:
        print('\n[red]Lintastic version was not specified.[/red]\n')
        sys.exit(1)
