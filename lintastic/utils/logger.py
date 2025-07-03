import os
import sys
from typing import NoReturn

from rich.console import Console


class Logger:
    console = Console(highlight=False)

    @staticmethod
    def info(message: str):
        Logger.console.print(f'[bold cyan]▶️  [INFO][/] {message}')

    @staticmethod
    def debug(message: str):
        if os.environ.get('LINTASTIC_VERBOSE') == 'true':
            Logger.console.print(f'[bold purple]🔎 [DEBUG][/] {message}')

    @staticmethod
    def success(message: str):
        Logger.console.print(f'[bold green]✅ [SUCCESS][/] {message}')

    @staticmethod
    def warning(message: str):
        Logger.console.print(f'[bold yellow]⚠️  [WARNING][/] {message}')

    @staticmethod
    def error(message: str, exit_program: bool = True) -> None | NoReturn:
        Logger.console.print(f'[bold red]❌ [ERROR][/] {message}')
        if exit_program:
            sys.exit(1)
