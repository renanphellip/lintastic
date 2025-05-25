
from lintastic.utils.logger import Logger
from lintastic.core.entities.diagnostic import DiagnosticCollection
from lintastic.core.enums.output_format import OutputFormat
from lintastic.core.interfaces.result_printer_factory import IResultPrinterFactory
from lintastic.core.interfaces.result_printer_service import IResultPrinterService


class ResultPrinterService(IResultPrinterService):
    def __init__(self, output_format: OutputFormat, result_printer_factory: IResultPrinterFactory):
        super().__init__(output_format, result_printer_factory)

    def print(self, diagnostic_collection: DiagnosticCollection) -> None:
        result_printer_strategy = self.result_printer_factory.get_result_printer_strategy(self.output_format)
        if result_printer_strategy is None:
            return
        Logger.info('Validation results:')
        result_printer_strategy.print(diagnostic_collection)
