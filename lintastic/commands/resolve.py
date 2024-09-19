from typing import Literal

import typer
from typing_extensions import Annotated

from ..file_writer import FileWriterService
from ..resolver import (
    DocumentResolveHandler,
)
from lintastic.utils.file_validator import FileValidator
from rich import print


def resolve(
    document_path: Annotated[
        str,
        typer.Argument(
            help=('Document path. Supported extensions: .yml, .yaml, .json')
        ),
    ],
    output_path: Annotated[
        str,
        typer.Argument(
            help=(
                'Resolved document path to be created. '
                'Supported extensions: .yml, .yaml, .json'
            )
        ),
    ],
    verbose: Annotated[
        bool,
        typer.Option(
            '--verbose', '-v', help='Verbose mode to display more logs.'
        ),
    ] = False,
) -> Literal[True]:
    if verbose:
        print()

    supported_extensions = ('.yml', '.yaml', '.json')
    file_validator = FileValidator()
    file_validator.validate_extension(
        document_path, supported_extensions, verbose
    )
    file_validator.validate_extension(
        output_path, supported_extensions, verbose
    )
    file_validator.validate_existence(document_path, verbose)

    document_resolve_handler = DocumentResolveHandler(verbose=verbose)
    resolved_document_data = document_resolve_handler.resolve(document_path)

    file_writer_service = FileWriterService()
    absolute_output_path = file_writer_service.write_file(
        output_path, resolved_document_data, verbose
    )

    print(
        f'\n[green]Successfully resolved document to: {absolute_output_path}[/green]\n'
    )

    return True
