import json
from dataclasses import asdict

from lintastic.core.entities.diagnostic import DiagnosticCollection
from lintastic.core.interfaces.result_printer_strategy import IResultPrinterStrategy
from rich.console import Console


class ResultJsonPrinterStrategy(IResultPrinterStrategy):
    def __init__(self):
        super().__init__()

    def print(self, diagnostic_collection: DiagnosticCollection) -> None:
        diagnostic_collection_json_string = json.dumps(
            asdict(diagnostic_collection), sort_keys=False, indent=2
        )
        self.console.print(f'\n[blue]{diagnostic_collection_json_string}[/]\n')
