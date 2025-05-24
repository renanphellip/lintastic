from abc import ABC, abstractmethod
from typing import Any, Dict

from lintastic.core.entities.diagnostic import DiagnosticCollection
from lintastic.core.interfaces.jsonpath_processor_service import IJSONPathProcessorService
from lintastic.core.interfaces.rule_processor_service import IRuleProcessorService


class IDocumentValidatorService(ABC):
    def __init__(
        self,
        rule_processor_service: IRuleProcessorService,
        jsonpath_processor_service: IJSONPathProcessorService,
    ):
        self.rule_processor_service = rule_processor_service
        self.jsonpath_processor_service = jsonpath_processor_service

    @abstractmethod
    def validate(self, document_data: Dict[str, Any]) -> DiagnosticCollection:
        pass
