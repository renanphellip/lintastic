from typing import Union

from lintastic.core.enums.output_format import OutputFormat
from lintastic.core.interfaces.result_printer_factory import IResultPrinterFactory
from lintastic.core.interfaces.result_printer_strategy import IResultPrinterStrategy
from lintastic.core.strategies.result_printer_strategy.result_json_printer_strategy import ResultJsonPrinterStrategy
from lintastic.core.strategies.result_printer_strategy.result_txt_printer_strategy import ResultTxtPrinterStrategy


class ResultPrinterFactory(IResultPrinterFactory):
    @staticmethod
    def get_result_printer_strategy(output_format: Union[OutputFormat, None]) -> Union[IResultPrinterStrategy, None]:
        if output_format == OutputFormat.TXT:
            return ResultTxtPrinterStrategy()
        elif output_format == OutputFormat.JSON:
            return ResultJsonPrinterStrategy()
        else:
            return None
