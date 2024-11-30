import json

import typer
from typing_extensions import Annotated

from lintastic.file_writer import FileWriterService
from lintastic.logs import Logger, LogMessages
from lintastic.resolver import (
    DocumentResolveHandler,
)
from lintastic.utils.file_validator import FileValidator


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
            '--verbose', '-v', help='Verbose mode to display debug logs.'
        ),
    ] = False,
):
    inputs = json.dumps({
        'document_path': document_path,
        'output_path': output_path,
        'verbose': verbose,
    })
    Logger.info(LogMessages.INPUTS.format(inputs=inputs))
    supported_extensions = ('.yml', '.yaml', '.json')
    FileValidator.validate_extension(
        document_path, supported_extensions, verbose
    )
    FileValidator.validate_extension(
        output_path, supported_extensions, verbose
    )
    FileValidator.validate_existence(document_path, verbose)

    document_resolve_handler = DocumentResolveHandler(verbose)
    resolved_document_data = document_resolve_handler.resolve(document_path)

    file_writer_service = FileWriterService(verbose)
    absolute_output_path = file_writer_service.write_file(
        output_path, resolved_document_data
    )

    Logger.success(
        LogMessages.DOCUMENT_RESOLVED.format(
            resolved_document_path=absolute_output_path
        )
    )
