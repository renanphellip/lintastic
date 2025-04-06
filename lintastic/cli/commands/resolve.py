import json

import typer
from typing_extensions import Annotated

from lintastic.core.enums.log_message import LogMessage
from lintastic.core.enums.supported_document_extension import (
    SupportedDocumentExtension,
)
from lintastic.core.resolver.document_resolve_handler import (
    DocumentResolveHandler,
)
from lintastic.io.writers.file_writer_service import FileWriterService
from lintastic.utils.file_validator import FileValidator
from lintastic.utils.logger import Logger


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
    # Init
    inputs = json.dumps({
        'document_path': document_path,
        'output_path': output_path,
        'verbose': verbose,
    })
    Logger.info(LogMessage.INPUTS.format(inputs=inputs))

    # Validation
    file_validator = FileValidator(verbose)
    file_validator.validate_extension(
        document_path, SupportedDocumentExtension
    )
    file_validator.validate_extension(output_path, SupportedDocumentExtension)
    file_validator.validate_existence(document_path)

    # Resolve
    document_resolve_handler = DocumentResolveHandler(verbose)
    resolved_document_data = document_resolve_handler.resolve(document_path)

    # Output
    file_writer_service = FileWriterService(verbose)
    absolute_output_path = file_writer_service.write_file(
        output_path, resolved_document_data
    )
    Logger.success(
        LogMessage.DOCUMENT_RESOLVED.format(
            resolved_document_path=absolute_output_path
        )
    )
