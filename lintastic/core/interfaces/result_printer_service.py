from abc import ABC, abstractmethod

from lintastic.core.entities.diagnostic import DiagnosticCollection
from lintastic.core.enums.output_format import OutputFormat
from lintastic.core.interfaces.result_printer_factory import IResultPrinterFactory


class IResultPrinterService(ABC):
    def __init__(self, output_format: OutputFormat, result_printer_factory: IResultPrinterFactory):
        self.output_format = output_format
        self.result_printer_factory = result_printer_factory

    @abstractmethod
    def print(self, diagnostic_collection: DiagnosticCollection) -> None:
        pass
