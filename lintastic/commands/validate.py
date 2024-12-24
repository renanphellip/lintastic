import json
from typing import Optional

import typer
from typing_extensions import Annotated

from lintastic.enums import LogMessage, OutputFormat
from lintastic.enums.supported_document_extension import (
    SupportedDocumentExtension,
)
from lintastic.enums.supported_output_extension import SupportedOutputExtension
from lintastic.utils.file_validator import FileValidator
from lintastic.utils.logger import Logger
from lintastic.validators.document_validator import DocumentValidator


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
                'Supported extensions: .json, .txt'
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
    inputs = json.dumps({
        'document_path': document_path,
        'ruleset_path': ruleset_path,
        'results_path': results_path,
        'output_format': output_format,
        'verbose': verbose,
    })
    Logger.info(LogMessage.INPUTS.format(inputs=inputs))
    file_validator = FileValidator(verbose)
    file_validator.validate_extension(
        document_path, SupportedDocumentExtension
    )
    file_validator.validate_extension(ruleset_path, SupportedDocumentExtension)
    if results_path:
        file_validator.validate_extension(
            results_path, SupportedOutputExtension
        )
    file_validator.validate_existence(document_path)
    file_validator.validate_existence(ruleset_path)
    document_validator = DocumentValidator(
        document_path, ruleset_path, 'custom_functions', verbose
    )
    document_validator.validate()
