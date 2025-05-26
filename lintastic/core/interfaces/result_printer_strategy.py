from abc import ABC, abstractmethod

from rich.console import Console

from lintastic.core.entities.diagnostic import DiagnosticCollection


class IResultPrinterStrategy(ABC):
    def __init__(self):
        self.console = Console(highlight=False)

    @abstractmethod
    def print(self, diagnostic_collection: DiagnosticCollection) -> None:
        pass
