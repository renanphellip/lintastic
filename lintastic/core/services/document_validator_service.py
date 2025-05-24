from typing import List

from rich.markup import escape

from lintastic.core.entities.diagnostic import Diagnostic, DiagnosticCollection
from lintastic.core.entities.rule import Rule
from lintastic.core.enums.log_message import LogMessage
from lintastic.core.interfaces.document_validator_service import IDocumentValidatorService
from lintastic.core.interfaces.jsonpath_processor_service import IJSONPathProcessorService
from lintastic.core.interfaces.rule_processor_service import IRuleProcessorService
from lintastic.utils.logger import Logger


class DocumentValidatorService(IDocumentValidatorService):
    def __init__(
        self,
        rule_processor_service: IRuleProcessorService,
        jsonpath_processor_service: IJSONPathProcessorService,
    ):
        super().__init__(rule_processor_service, jsonpath_processor_service)

    def validate(self, rules: List[Rule]) -> DiagnosticCollection:
        try:
            diagnostics: List[Diagnostic] = []
            for rule in rules:
                Logger.info(LogMessage.PROCESSING_RULE.format(rule_name=rule.name))
                jsonpath_matches = self.jsonpath_processor_service.process(rule)
                diagnostics.extend(self.rule_processor_service.process(rule, jsonpath_matches))

            return DiagnosticCollection(diagnostics)

        except Exception as error:
            Logger.error(LogMessage.FAIL_TO_VALIDATE_DOCUMENT.format(document_path=self.document_path, error=escape(str(error))))
