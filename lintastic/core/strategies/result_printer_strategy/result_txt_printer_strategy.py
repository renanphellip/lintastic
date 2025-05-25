from lintastic.core.entities.diagnostic import DiagnosticCollection
from lintastic.core.enums.severity import Severity
from lintastic.core.interfaces.result_printer_strategy import IResultPrinterStrategy


class ResultTxtPrinterStrategy(IResultPrinterStrategy):
    def __init__(self):
        super().__init__()

    def print(self, diagnostic_collection: DiagnosticCollection) -> None:
        self.console.print('')
        for diagnostic in diagnostic_collection.diagnostics:
            severity_color_mapping = {
                Severity.ERROR: '[bold red]Error',
                Severity.WARN: '[bold yellow]Warning',
                Severity.INFO: '[bold cyan]Information',
                Severity.HINT: '[bold green]Hint',
            }
            self.console.print(f'Rule: [bold]{diagnostic.rule}[/]')
            self.console.print(f'Severity: {severity_color_mapping[diagnostic.severity]}[/]')
            self.console.print(f'Context: [bold]{diagnostic.context}[/]')
            self.console.print('Messages:')
            for message in diagnostic.messages:
                self.console.print(f'- {message}')
            if diagnostic.documentations:
                self.console.print('Documentations:')
                for doc in diagnostic.documentations:
                    self.console.print(f'- {doc}')
            self.console.print('')

        self.console.print('[bold]Summary:[/]')
        self.console.print(f'[bold red]- Total Errors: {diagnostic_collection.summary.total_errors}[/]')
        self.console.print(f'[bold yellow]- Total Warnings: {diagnostic_collection.summary.total_warnings}[/]')
        self.console.print(f'[bold cyan]- Total Informations: {diagnostic_collection.summary.total_informations}[/]')
        self.console.print(f'[bold green]- Total Hints: {diagnostic_collection.summary.total_hints}[/]')
        self.console.print('')
