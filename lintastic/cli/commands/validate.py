import json
from typing import Optional

import typer
from typing_extensions import Annotated

from lintastic.core.enums.log_message import LogMessage
from lintastic.core.enums.output_format import OutputFormat
from lintastic.core.enums.supported_document_extension import (
    SupportedDocumentExtension,
)
from lintastic.core.enums.supported_result_extension import (
    SupportedResultExtension,
)
from lintastic.core.validators.document_validator import DocumentValidator
from lintastic.io.writers.file_writer_service import FileWriterService
from lintastic.utils.file_validator import FileValidator
from lintastic.utils.logger import Logger


def validate(
    document_path: Annotated[
        str,
        typer.Argument(
            help=('Document path. Supported extensions: .yml, .yaml, .json')
        ),
    ],
    ruleset_path: Annotated[
        str,
        typer.Argument(
            help=('Ruleset path. Supported extensions: .yml, .yaml, .json')
        ),
    ],
    results_path: Annotated[
        Optional[str],
        typer.Argument(
            help=(
                'Validation results file path to be created. '
                'Supported extensions: .json, .txt, .md'
            )
        ),
    ] = None,
    output_format: Annotated[
        OutputFormat,
        typer.Option(
            '--output-format',
            '-f',
            help=(
                'Output format of results in the console. '
                'This option does not affect the results_path argument.'
            ),
            case_sensitive=False,
        ),
    ] = OutputFormat.TXT,
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
        'ruleset_path': ruleset_path,
        'results_path': results_path,
        'output_format': output_format,
        'verbose': verbose,
    })
    Logger.info(LogMessage.INPUTS.format(inputs=inputs))

    # Validation
    file_validator = FileValidator(verbose)
    file_validator.validate_extension(
        document_path, SupportedDocumentExtension
    )
    file_validator.validate_extension(ruleset_path, SupportedDocumentExtension)
    if results_path:
        file_validator.validate_extension(
            results_path, SupportedResultExtension
        )
    file_validator.validate_existence(document_path)
    file_validator.validate_existence(ruleset_path)

    # Validate
    document_validator = DocumentValidator(
        document_path, ruleset_path, 'custom_functions', verbose
    )
    diagnostic_collection = document_validator.validate()

    # Output
    if results_path:
        file_writer_service = FileWriterService(verbose)
        absolute_results_path = file_writer_service.write_file(
            results_path, diagnostic_collection
        )
        Logger.success(
            LogMessage.RESULTS_EXPORTED.format(
                results_path=absolute_results_path
            )
        )
