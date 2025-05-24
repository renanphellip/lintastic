import json
from typing import Optional

import typer
from typing_extensions import Annotated

from lintastic.cli.callbacks.validate_document_path import validate_document_path
from lintastic.cli.callbacks.validate_results_path import validate_results_path
from lintastic.cli.dto.validate_inputs_dto import ValidateInputsDTO
from lintastic.core.enums.log_message import LogMessage
from lintastic.core.enums.output_format import OutputFormat
from lintastic.core.handlers.validate_handler import ValidateHandler
from lintastic.utils.logger import Logger


def validate(
    document_path: Annotated[
        str,
        typer.Argument(help=('Document path. Supported extensions: .yml, .yaml, .json'), callback=validate_document_path),
    ],
    ruleset_path: Annotated[
        str,
        typer.Argument(help=('Ruleset path. Supported extensions: .yml, .yaml, .json'), callback=validate_document_path),
    ],
    results_path: Annotated[
        Optional[str],
        typer.Argument(help=('Validation results file path to be created. ' 'Supported extensions: .json, .txt, .md'), callback=validate_results_path),
    ] = None,
    output_format: Annotated[
        OutputFormat,
        typer.Option(
            '--output-format',
            '-f',
            help=('Output format of results in the console. ' 'This option does not affect the results_path argument.'),
            case_sensitive=False,
        ),
    ] = OutputFormat.TXT,
    verbose: Annotated[
        bool,
        typer.Option('--verbose', '-v', help='Verbose mode to display debug logs.'),
    ] = False,
):
    inputs = ValidateInputsDTO(
        document_path=document_path,
        ruleset_path=ruleset_path,
        results_path=results_path,
        output_format=output_format,
        verbose=verbose,
    )
    inputs_json_string = json.dumps(inputs.__dict__, indent=2)
    Logger.info(LogMessage.INPUTS.format(inputs=inputs_json_string))
    ValidateHandler.execute(inputs)
