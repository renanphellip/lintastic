from typing import Any, Dict, List

from rich.markup import escape

from lintastic.entities.diagnostic import Diagnostic, DiagnosticCollection
from lintastic.enums.log_message import LogMessage
from lintastic.functions.function_importer_service import (
    FunctionImporterService,
)
from lintastic.readers.file_reader_service import FileReaderService
from lintastic.resolver.document_resolve_handler import DocumentResolveHandler
from lintastic.ruleset.ruleset import Ruleset
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

    def __import_functions(self) -> Dict[str, Any]:
        core_functions = FunctionImporterService(
            'lintastic/functions'
        ).import_functions()
        for function_name, function in core_functions.items():
            globals()[function_name] = function
        
        custom_functions = FunctionImporterService(
            self.custom_functions_path, self.verbose, globals()
        ).import_functions()
        for function_name, function in custom_functions.items():
            globals()[function_name] = function
        return globals()

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
