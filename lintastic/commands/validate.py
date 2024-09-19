from typing import Optional

import typer
from typing_extensions import Annotated

from lintastic.entities.validator import OutputFormat
from lintastic.utils.file_validator import FileValidator
from rich import print


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
            '--verbose', '-v', help='Verbose mode to display more logs.'
        ),
    ] = False,
):
    if verbose:
        print()

    supported_extensions = ('.yml', '.yaml', '.json')
    results_supported_extensions = ('.txt', '.json')
    file_validator = FileValidator()
    file_validator.validate_extension(
        document_path, supported_extensions, verbose
    )
    file_validator.validate_extension(
        ruleset_path, supported_extensions, verbose
    )
    if results_path:
        file_validator.validate_extension(
            results_path, results_supported_extensions, verbose
        )
    file_validator.validate_existence(document_path, verbose)
    file_validator.validate_existence(ruleset_path, verbose)

    absolute_output_path = 'xpto'
    print(
        f'\nCheck the validation results at: [blue]{absolute_output_path}[/blue]\n'
    )

    return True
