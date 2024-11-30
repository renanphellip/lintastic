import json
from typing import Optional

import typer
from typing_extensions import Annotated

from lintastic.logs import Logger, LogMessages
from lintastic.utils.file_validator import FileValidator
from lintastic.utils.output_format import OutputFormat
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
    Logger.info(LogMessages.INPUTS.format(inputs=inputs))
    supported_extensions = ('.yml', '.yaml', '.json')
    results_supported_extensions = ('.txt', '.json')
    FileValidator.validate_extension(
        document_path, supported_extensions, verbose
    )
    FileValidator.validate_extension(
        ruleset_path, supported_extensions, verbose
    )
    if results_path:
        FileValidator.validate_extension(
            results_path, results_supported_extensions, verbose
        )
    FileValidator.validate_existence(document_path, verbose)
    FileValidator.validate_existence(ruleset_path, verbose)
    document_validator = DocumentValidator(
        document_path, ruleset_path, 'custom_functions', verbose
    )
    document_validator.validate()
