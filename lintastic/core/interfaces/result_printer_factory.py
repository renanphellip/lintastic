from abc import ABC, abstractmethod
from typing import Union

from lintastic.core.enums.output_format import OutputFormat
from lintastic.core.interfaces.result_printer_strategy import IResultPrinterStrategy


class IResultPrinterFactory(ABC):
    @abstractmethod
    def get_result_printer_strategy(self, output_format: Union[OutputFormat, None]) -> Union[IResultPrinterStrategy, None]:
        pass
