import sys

from rich.console import Console

from lintastic.file_writer.file_writer import IFileWriter
from lintastic.file_writer.json_file_writer import JsonFileWriter
from lintastic.file_writer.txt_file_writer import TxtFileWriter
from lintastic.file_writer.yaml_file_writer import YamlFileWriter


class FileWriterFactory:
    @staticmethod
    def get_file_writer(output_path: str) -> IFileWriter:
        output_path = output_path.lower()
        if output_path.endswith('.txt'):
            return TxtFileWriter()
        elif output_path.endswith('.json'):
            return JsonFileWriter()
        elif output_path.endswith(('yaml', 'yml')):
            return YamlFileWriter()
        else:
            console = Console(highlight=False)
            console.print(
                f'[red]Unsupported file extension: {output_path}[/red]'
            )
            sys.exit(1)
