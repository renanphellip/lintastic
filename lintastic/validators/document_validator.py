from rich.markup import escape

from lintastic.entities.diagnostic import DiagnosticCollection
from lintastic.enums.log_message import LogMessage
from lintastic.functions.function_importer_service import (
    FunctionImporterService,
)
from lintastic.ruleset.ruleset import Ruleset
from lintastic.utils.document_data_loader import DocumentDataLoader
from lintastic.utils.logger import Logger
from lintastic.validators.function_validator import FunctionValidator
from lintastic.validators.rule_processor import RuleProcessor


class DocumentValidator:
    def __init__(
        self,
        document_path: str,
        ruleset_path: str,
        custom_functions_path: str,
        verbose=False,
    ):
        self.document_path = document_path
        self.ruleset_path = ruleset_path
        self.custom_functions_path = custom_functions_path
        self.verbose = verbose
        self.document_data_loader = DocumentDataLoader(document_path, verbose)
        self.rule_processor = RuleProcessor(verbose)

    def validate(self) -> DiagnosticCollection:
        try:
            ruleset = Ruleset(self.ruleset_path, self.verbose)
            FunctionImporterService(
                self.custom_functions_path, self.verbose
            ).import_functions()
            rules = ruleset.get_rules()
            FunctionValidator(rules, globals()).validate_functions()

            resolve_refs = any(rule.resolved for rule in rules)
            document_data = self.document_data_loader.load(resolve_refs)

            diagnostics = []
            for rule in rules:
                jsonpath_matches = self.rule_processor.get_jsonpath_matches(
                    rule, document_data
                )
                diagnostics.extend(
                    self.rule_processor.process(rule, jsonpath_matches)
                )

            return DiagnosticCollection(diagnostics)

        except Exception as error:
            Logger.error(
                LogMessage.FAIL_TO_VALIDATE_DOCUMENT.format(
                    document_path=self.document_path, error=escape(str(error))
                )
            )
