from typing import Literal

import typer
from typing_extensions import Annotated

from lintastic.file_writer.file_writer_service import FileWriterService
from lintastic.resolver.document_resolver_service import DocumentResolverService
from lintastic.utils.file_validator import FileValidator


def resolve(
    document_path: Annotated[
        str,
        typer.Argument(
            help=('Document path. ' 'Supported extensions: .yml, .yaml, .json')
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
    supported_extensions = ('.yml', '.yaml', '.json')
    file_validator = FileValidator()
    file_validator.validate_existence(document_path, verbose)
    file_validator.validate_extension(output_path, supported_extensions, verbose)
    
    document_resolver_service = DocumentResolverService(verbose=verbose)
    resolved_document_data = document_resolver_service.resolve(document_path)

    file_writer_service = FileWriterService()
    file_writer_service.write_file(output_path, resolved_document_data, verbose)
    
    return True
