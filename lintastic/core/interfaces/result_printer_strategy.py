from abc import ABC, abstractmethod

from lintastic.core.entities.diagnostic import DiagnosticCollection
from rich.console import Console


class IResultPrinterStrategy(ABC):
    def __init__(self):
        self.console = Console(highlight=False)
    
    @abstractmethod
    def print(self, diagnostic_collection: DiagnosticCollection) -> None:
        pass
