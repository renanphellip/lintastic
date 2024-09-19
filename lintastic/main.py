#!/usr/bin/env python3

import typer

from .commands import *

cli = typer.Typer(help='Lintastic', no_args_is_help=True)
cli.command(help='Show Lintastic CLI version')(version)
cli.command(help='Resolve YAML external references')(resolve)
cli.command(help='Validate ruleset to YAML or JSON document')(validate)

if __name__ == '__main__':
    cli()
