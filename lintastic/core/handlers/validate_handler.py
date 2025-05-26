import os
from typing import Any, Dict, List

from lintastic.cli.dto.validate_inputs_dto import ValidateInputsDTO
from lintastic.core.entities.diagnostic import DiagnosticCollection
from lintastic.core.entities.rule import Rule
from lintastic.core.enums.log_message import LogMessage
from lintastic.core.enums.output_format import OutputFormat
from lintastic.core.factories.result_printer_factory import ResultPrinterFactory
from lintastic.core.factories.rule_factory import RuleFactory
from lintastic.core.services.document_resolver_service import DocumentResolverService
from lintastic.core.services.document_validator_service import DocumentValidatorService
from lintastic.core.services.function_importer_service import FunctionImporterService
from lintastic.core.services.function_validator_service import FunctionValidatorService
from lintastic.core.services.jsonpath_processor_service import JSONPathProcessorService
from lintastic.core.services.ref_resolver_service import RefResolverService
from lintastic.core.services.result_printer_service import ResultPrinterService
from lintastic.core.services.rule_processor_service import RuleProcessorService
from lintastic.core.services.ruleset_loader_service import RulesetLoaderService
from lintastic.io.readers.file_reader_service import FileReaderService
from lintastic.io.writers.file_writer_service import FileWriterService
from lintastic.utils.logger import Logger


class ValidateHandler:
    def __init__(self):
        self.file_reader_service = FileReaderService()
        self.globals = globals()

    def execute(self, inputs: ValidateInputsDTO) -> None:
        # Set verbose mode if specified
        self._set_verbose(inputs.verbose)

        # Import core and custom functions
        self._import_functions(functions_path='lintastic/core/functions/core')
        self._import_functions(functions_path='lintastic/core/functions/custom')

        # Load the ruleset
        rules = self._load_ruleset(inputs.ruleset_path)

        # Validate imported functions against the ruleset
        self._validate_functions(rules)

        # Resolve the document
        document_data = self._resolve_document(rules, inputs.document_path)

        # Validate the document with the rules
        diagnostic_collection = self._validate_document(rules, inputs.document_path, document_data)

        # Terminal output
        self._print_results(diagnostic_collection, inputs.output_format)

        # File output
        self._write_results(diagnostic_collection, inputs.results_path)

        # Exit
        Logger.info(LogMessage.VALIDATION_COMPLETED)

    @staticmethod
    def _set_verbose(verbose: bool) -> None:
        if verbose:
            os.environ['LINTASTIC_VERBOSE'] = 'true'

    def _import_functions(self, functions_path: str) -> None:
        function_importer_service = FunctionImporterService(self.globals)
        functions = function_importer_service.import_functions(functions_path)
        for function_name, function in functions.items():
            self.globals[function_name] = function

    def _load_ruleset(self, ruleset_path: str) -> List[Rule]:
        rule_factory = RuleFactory()
        ruleset_loader_service = RulesetLoaderService(self.file_reader_service, rule_factory)
        ruleset_loader_service.load_ruleset(ruleset_path)
        return ruleset_loader_service.get_rules()

    def _validate_functions(self, rules: List[Rule]) -> None:
        function_validator_service = FunctionValidatorService(self.globals)
        function_validator_service.validate_functions(rules)

    def _resolve_document(self, rules: List[Rule], document_path: str) -> Dict[str, Any]:
        resolve_refs = any(rule.resolved for rule in rules)
        if resolve_refs:
            ref_resolver_service = RefResolverService(self.file_reader_service)
            document_resolver_service = DocumentResolverService(self.file_reader_service, ref_resolver_service)
            return document_resolver_service.resolve(document_path)
        else:
            return self.file_reader_service.read_file(document_path)

    def _validate_document(self, rules: List[Rule], document_path: str, document_data: Dict[str, Any]) -> DiagnosticCollection:
        rule_processor_service = RuleProcessorService(self.globals)
        jsonpath_processor_service = JSONPathProcessorService(document_data)
        document_validator_service = DocumentValidatorService(rule_processor_service, jsonpath_processor_service)
        return document_validator_service.validate(rules, document_path)

    @staticmethod
    def _print_results(diagnostic_collection: DiagnosticCollection, output_format: OutputFormat) -> None:
        result_printer_factory = ResultPrinterFactory()
        result_printer_service = ResultPrinterService(output_format, result_printer_factory)
        result_printer_service.print(diagnostic_collection)

    @staticmethod
    def _write_results(diagnostic_collection: DiagnosticCollection, results_path: str) -> None:
        if results_path:
            file_writer_service = FileWriterService()
            absolute_results_path = file_writer_service.write_file(results_path, diagnostic_collection)
            Logger.info(LogMessage.RESULTS_EXPORTED.format(results_path=absolute_results_path))
