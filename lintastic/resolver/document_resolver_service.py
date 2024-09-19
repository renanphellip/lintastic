import sys
from pathlib import Path
from typing import Any, Dict

from rich.console import Console
from rich.markup import escape

from lintastic.file_reader.file_reader_service import FileReaderService
from lintastic.resolver.ref_resolver import RefResolver


class DocumentResolverService:
    def __init__(
        self,
        file_reader_service=FileReaderService(),
        verbose=False,
        console=Console(highlight=False),
    ):
        self.file_reader_service = file_reader_service
        self.verbose = verbose
        self.console = console
        self.ref_resolver = RefResolver(file_reader_service, verbose)

    def resolve(self, document_path: str) -> Dict[str, Any]:
        try:
            document_base_path = Path(document_path).parent
            document_data = self.file_reader_service.read_file(
                document_path, self.verbose
            )

            if self.verbose:
                self.console.print(f'Resolving: [blue]{document_path}[/blue]')

            resolved_document_data = self.ref_resolver.resolve(
                document_data, document_base_path
            )
            return resolved_document_data

        except Exception as error:
            self.console.print(
                f'[red]Failed to resolve: {document_path}\n'
                f'{escape(str(error))}[/red]'
            )
            sys.exit(1)
