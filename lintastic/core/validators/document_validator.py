from typing import Any, Dict, List

from rich.markup import escape

from lintastic.core.entities.diagnostic import Diagnostic, DiagnosticCollection
from lintastic.core.enums.log_message import LogMessage
from lintastic.core.functions.core.function_importer_service import (
    FunctionImporterService,
)
from lintastic.core.resolver.document_resolve_handler import (
    DocumentResolveHandler,
)
from lintastic.core.ruleset.ruleset import Ruleset
from lintastic.core.validators.function_validator import FunctionValidator
from lintastic.core.validators.rule_processor import RuleProcessor
from lintastic.io.readers.file_reader_service import FileReaderService
from lintastic.utils.logger import Logger


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

    def validate(self) -> DiagnosticCollection:
        try:
            ruleset = Ruleset(self.ruleset_path, self.verbose)
            imported_functions = self.__import_functions()
            rules = ruleset.get_rules()
            FunctionValidator(rules, imported_functions).validate_functions()
            rule_processor = RuleProcessor(globals(), self.verbose)

            resolve_refs = any(rule.resolved for rule in rules)
            document_data = self.__get_document_data(resolve_refs)

            diagnostics: List[Diagnostic] = []
            for rule in rules:
                Logger.info(
                    LogMessage.PROCESSING_RULE.format(rule_name=rule.name)
                )
                jsonpath_matches = rule_processor.get_jsonpath_matches(
                    rule, document_data
                )
                diagnostics.extend(
                    rule_processor.process(rule, jsonpath_matches)
                )

            return DiagnosticCollection(diagnostics)

        except Exception as error:
            Logger.error(
                LogMessage.FAIL_TO_VALIDATE_DOCUMENT.format(
                    document_path=self.document_path, error=escape(str(error))
                )
            )

    def __import_functions(self) -> Dict[str, Any]:
        core_functions = FunctionImporterService(
            'lintastic/core/functions/core'
        ).import_functions()
        for function_name, function in core_functions.items():
            globals()[function_name] = function

        custom_functions = FunctionImporterService(
            self.custom_functions_path, self.verbose, globals()
        ).import_functions()
        for function_name, function in custom_functions.items():
            globals()[function_name] = function
        return globals()

    def __get_document_data(self, resolve_refs: bool) -> Dict[str, Any]:
        document_data = {}
        if resolve_refs:
            document_resolve_handler = DocumentResolveHandler(self.verbose)
            document_data = document_resolve_handler.resolve(
                self.document_path
            )
        else:
            file_reader_service = FileReaderService(self.verbose)
            document_data = file_reader_service.read_file(self.document_path)
        return document_data
