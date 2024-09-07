from typing import Optional

import typer
from typing_extensions import Annotated

from lintastic.entities.validator import OutputFormat


def validate(
    document_path: Annotated[
        str,
        typer.Argument(
            help=(
                'Document path. '
                'Supported extensions: .yml, .yaml, .json'
            )
        ),
    ],
    ruleset_path: Annotated[
        str,
        typer.Argument(
            help=(
                'Ruleset path. '
                'Supported extensions: .yml, .yaml, .json'
            )
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
    return True
