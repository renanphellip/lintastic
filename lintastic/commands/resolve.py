from typing import Literal

import typer
from typing_extensions import Annotated


def resolve(
    document_path: Annotated[
        str,
        typer.Argument(
            help=('Document path. ' 'Supported extensions: .yml, .yaml')
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
    return True
