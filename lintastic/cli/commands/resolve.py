import json

import typer
from typing_extensions import Annotated

from lintastic.cli.callbacks.validate_document_path import validate_document_path
from lintastic.cli.callbacks.validate_output_path import validate_output_path
from lintastic.cli.dto.resolve_inputs_dto import ResolveInputsDTO
from lintastic.core.enums.log_message import LogMessage
from lintastic.core.handlers.resolve_handler import ResolveHandler
from lintastic.utils.logger import Logger


def resolve(
    document_path: Annotated[
        str,
        typer.Argument(help=('Document path. Supported extensions: .yml, .yaml, .json'), callback=validate_document_path),
    ],
    output_path: Annotated[
        str,
        typer.Argument(help=('Resolved document path to be created. ' 'Supported extensions: .yml, .yaml, .json'), callback=validate_output_path),
    ],
    verbose: Annotated[
        bool,
        typer.Option('--verbose', '-v', help='Verbose mode to display debug logs.'),
    ] = False,
):
    inputs = ResolveInputsDTO(
        document_path=document_path,
        output_path=output_path,
        verbose=verbose,
    )
    inputs_json_string = json.dumps(inputs.__dict__, indent=2)
    Logger.info(LogMessage.INPUTS.format(inputs=inputs_json_string))
    ResolveHandler.execute(inputs)
