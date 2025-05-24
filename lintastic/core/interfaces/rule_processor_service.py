from abc import ABC, abstractmethod
from typing import Any, Dict, List

from lintastic.core.entities.diagnostic import Diagnostic
from lintastic.core.entities.jsonpath_match import JSONPathMatch
from lintastic.core.entities.rule import Rule


class IRuleProcessorService(ABC):
    def __init__(self, globals: Dict[str, Any]):
        self.globals = globals

    @abstractmethod
    def process(self, rule: Rule, jsonpath_matches: List[JSONPathMatch]) -> List[Diagnostic]:
        pass
