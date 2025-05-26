from abc import ABC, abstractmethod
from typing import Any, Dict


class IFunctionImporterService(ABC):
    def __init__(
        self,
        globals: Dict[str, Any],
    ):
        self.globals = globals

    @abstractmethod
    def import_functions(self, functions_path: str) -> Dict[str, Any]:
        pass
