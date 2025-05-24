from abc import ABC, abstractmethod
from typing import Any, Dict, List

from lintastic.core.entities.jsonpath_match import JSONPathMatch
from lintastic.core.entities.rule import Rule


class IJSONPathProcessorService(ABC):
    def __init__(self, document_data: Dict[str, Any]):
        self.document_data = document_data

    @abstractmethod
    def process(rule: Rule) -> List[JSONPathMatch]:
        pass
