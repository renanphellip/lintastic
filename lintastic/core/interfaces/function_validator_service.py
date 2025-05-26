from abc import ABC, abstractmethod
from typing import Any, Dict, List

from lintastic.core.entities.rule import Rule


class IFunctionValidatorService(ABC):
    def __init__(self, globals: Dict[str, Any]):
        self.globals = globals

    @abstractmethod
    def validate_functions(self, rules: List[Rule]) -> None:
        pass
