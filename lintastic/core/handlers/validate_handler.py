import os

from lintastic.cli.dto.validate_inputs_dto import ValidateInputsDTO
from lintastic.core.enums.log_message import LogMessage
from lintastic.core.services.function_importer_service import FunctionImporterService
from lintastic.core.services.jsonpath_processor_service import JSONPathProcessorService
from lintastic.core.services.rule_processor_service import RuleProcessorService
from lintastic.core.services.document_resolver_service import DocumentResolverService
from lintastic.core.services.ref_resolver_service import RefResolverService
from lintastic.core.factories.rule_factory import RuleFactory
from lintastic.core.services.ruleset_loader_service import RulesetLoaderService
from lintastic.core.validators.document_validator_service import DocumentValidatorService
from lintastic.core.validators.function_validator_service import FunctionValidatorService
from lintastic.io.readers.file_reader_service import FileReaderService
from lintastic.io.writers.file_writer_service import FileWriterService
from lintastic.utils.logger import Logger


class ValidateHandler:
    @staticmethod
    def execute(inputs: ValidateInputsDTO) -> None:
        # Verbose
        if inputs.verbose:
            os.environ['LINTASTIC_VERBOSE'] = 'true'

        # Core Functions
        function_importer_service = FunctionImporterService(globals())
        core_functions = function_importer_service.import_functions('lintastic/core/functions/core')
        for function_name, function in core_functions.items():
            globals()[function_name] = function

        # Custom Functions
        function_importer_service.globals = globals()
        custom_functions = function_importer_service.import_functions('lintastic/core/functions/custom')
        for function_name, function in custom_functions.items():
            globals()[function_name] = function

        # Ruleset
        file_reader_service = FileReaderService()
        rule_factory = RuleFactory()
        ruleset_loader_service = RulesetLoaderService(file_reader_service, rule_factory)
        ruleset_loader_service.load_ruleset(inputs.ruleset_path)
        rules = ruleset_loader_service.get_rules()

        # Function Validation
        function_validator_service = FunctionValidatorService(globals())
        function_validator_service.validate_functions(rules)

        # Document Resolution
        resolve_refs = any(rule.resolved for rule in rules)
        document_data = {}
        if resolve_refs:
            ref_resolver_service = RefResolverService(file_reader_service)
            document_resolver_service = DocumentResolverService(file_reader_service, ref_resolver_service)
            document_data = document_resolver_service.resolve(inputs.document_path)
        else:
            document_data = file_reader_service.read_file(inputs.document_path)

        # Document Validation
        rule_processor_service = RuleProcessorService(globals())
        jsonpath_processor_service = JSONPathProcessorService(document_data)
        document_validator_service = DocumentValidatorService(rules, rule_processor_service, jsonpath_processor_service)
        diagnostic_collection = document_validator_service.validate(document_data)

        # Output
        if inputs.results_path:
            file_writer_service = FileWriterService()
            absolute_results_path = file_writer_service.write_file(inputs.results_path, diagnostic_collection)
            Logger.success(LogMessage.RESULTS_EXPORTED.format(results_path=absolute_results_path))
