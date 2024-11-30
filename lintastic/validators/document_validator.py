from typing import Any, Dict

from lintastic.file_reader.file_reader_service import FileReaderService
from lintastic.function_importer.function_importer_service import (
    FunctionImporter,
)
from lintastic.resolver.document_resolve_handler import DocumentResolveHandler
from lintastic.ruleset.ruleset import Ruleset
from lintastic.validators.function_validator import FunctionValidator


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

    def __get_document_data(self, resolve_contract: bool) -> Dict[str, Any]:
        resolved_document_data = {}
        if resolve_contract:
            document_resolve_handler = DocumentResolveHandler(self.verbose)
            resolved_document_data = document_resolve_handler.resolve(
                self.document_path
            )
        else:
            file_reader_service = FileReaderService(self.verbose)
            resolved_document_data = file_reader_service.read_file(
                self.document_path
            )
        return resolved_document_data

    def validate(self):
        ruleset = Ruleset(self.ruleset_path, self.verbose)

        function_importer = FunctionImporter(
            self.custom_functions_path, self.verbose
        )
        function_importer.import_functions()

        rules = ruleset.get_rules()

        function_validator = FunctionValidator(rules, globals())
        function_validator.validate_functions()

        resolve_contract = any(rule.resolved for rule in rules)

        resolved_document_data = self.__get_document_data(resolve_contract)
        return resolved_document_data
