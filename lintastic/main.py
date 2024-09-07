#!/usr/bin/env python3

import typer

from lintastic.commands.resolve import resolve
from lintastic.commands.validate import validate
from lintastic.commands.version import version

cli = typer.Typer(help='Lintastic', no_args_is_help=True)
cli.command(help='Show Lintastic CLI version')(version)
cli.command(help='Resolve YAML external references')(resolve)
cli.command(help='Validate ruleset to YAML or JSON document')(validate)

if __name__ == '__main__':
    cli()
