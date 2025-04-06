#!/usr/bin/env python3

import typer

from lintastic.cli.commands import resolve, validate, version

cli = typer.Typer(help='Lintastic', no_args_is_help=True)
cli.command(help='Show Lintastic CLI version')(version)
cli.command(help='Resolve YAML/JSON external references')(resolve)
cli.command(help='Validate ruleset to YAML/JSON document')(validate)

if __name__ == '__main__':
    cli()
