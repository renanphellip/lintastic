import sys

from rich.console import Console


class Logger:
    _console = Console(highlight=False)

    @staticmethod
    def info(message: str):
        Logger._console.print(f'[bold cyan][INFO][/] {message}')

    @staticmethod
    def debug(message: str):
        Logger._console.print(f'[bold purple][DEBUG][/] {message}')

    @staticmethod
    def success(message: str):
        Logger._console.print(f'[bold green][SUCCESS][/] {message}')

    @staticmethod
    def warning(message: str):
        Logger._console.print(f'[bold yellow][WARNING][/] {message}')

    @staticmethod
    def error(message: str, exit_program=True):
        Logger._console.print(f'[bold red][ERROR][/] {message}')
        if exit_program:
            sys.exit(1)
