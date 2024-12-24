from typing import Any, Callable, Dict, List, Union

from rich.markup import escape

from lintastic.entities.diagnostic import Diagnostic, DiagnosticCollection
from lintastic.entities.functions import (
    AlphabeticalRuleThen,
    CasingRuleThen,
    CustomRuleThen,
    DefinedRuleThen,
    EnumerationRuleThen,
    FalsyRuleThen,
    LengthRuleThen,
    PatternRuleThen,
    SchemaRuleThen,
    TruthyRuleThen,
    TypedEnumRuleThen,
    UndefinedRuleThen,
    UnreferencedReusableObjectRuleThen,
    XORRuleThen,
)
from lintastic.entities.jsonpath import JSONPathMatch
from lintastic.entities.rule import Rule
from lintastic.enums import LogMessage
from lintastic.functions.function_importer_service import (
    FunctionImporterService,
)
from lintastic.readers.file_reader_service import FileReaderService
from lintastic.resolver.document_resolve_handler import DocumentResolveHandler
from lintastic.ruleset.ruleset import Ruleset
from lintastic.utils.logger import Logger
from lintastic.validators.function_validator import FunctionValidator
from lintastic.validators.jsonpath_validator import JSONPathValidator


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
        document_data = {}
        if resolve_contract:
            document_resolve_handler = DocumentResolveHandler(self.verbose)
            document_data = document_resolve_handler.resolve(
                self.document_path
            )
        else:
            file_reader_service = FileReaderService(self.verbose)
            document_data = file_reader_service.read_file(self.document_path)
        return document_data

    def __get_jsonpath_matches_from_rule(
        self, rule: Rule, document_data: Dict[str, Any]
    ) -> List[JSONPathMatch]:
        results: List[JSONPathMatch] = []
        for jsonpath in rule.given:
            jsonpath_validator = JSONPathValidator(
                jsonpath, document_data, self.verbose
            )
            results.extend(jsonpath_validator.validate())
        return results

    def __get_field_name_from_rule_then(
        self, jsonpath_match: JSONPathMatch, rule_then: Any
    ) -> str:
        if hasattr(rule_then, 'field'):
            return rule_then.field
        else:
            return jsonpath_match.context.split('.')[-1]

    def __run_function(
        self,
        rule: Rule,
        rule_then: Union[
            AlphabeticalRuleThen,
            CasingRuleThen,
            DefinedRuleThen,
            EnumerationRuleThen,
            FalsyRuleThen,
            LengthRuleThen,
            PatternRuleThen,
            SchemaRuleThen,
            TruthyRuleThen,
            TypedEnumRuleThen,
            UndefinedRuleThen,
            UnreferencedReusableObjectRuleThen,
            XORRuleThen,
            CustomRuleThen,
        ],
        rule_function: Callable,
        jsonpath_match: JSONPathMatch,
        field: str,
    ) -> Diagnostic | None:
        if self.verbose:
            escaped_jsonpath_match = escape(str(jsonpath_match))
            Logger.debug(
                LogMessage.RUNNING_FUNCTION.format(
                    function_name=rule_then.function,
                    jsonpath_match=escaped_jsonpath_match,
                )
            )
        function_messages: List[str] = []
        function_messages.extend(
            rule_function(
                jsonpath_match.context,
                jsonpath_match.target_value,
                rule_then.function_options,
                field,
                self.verbose,
                rule.name,
            )
        )
        if function_messages:
            return Diagnostic(
                rule.name,
                jsonpath_match.context,
                rule.severity,
                function_messages,
                rule.documentation,
            )
        return None

    def __process_rule(
        self,
        rule: Rule,
        jsonpath_matches: List[JSONPathMatch],
    ) -> List[Diagnostic]:
        if self.verbose:
            Logger.debug(
                LogMessage.PROCESSING_RULE.format(rule_name=rule.name)
            )
        diagnostics: List[Diagnostic] = []
        for jsonpath_match in jsonpath_matches:
            if isinstance(rule.then, list):
                for item in rule.then:
                    field = self.__get_field_name_from_rule_then(
                        jsonpath_match, item
                    )
                    rule_function = globals().get(item.function)
                    diagnostics.append(
                        self.__run_function(
                            rule,
                            item,
                            rule_function,
                            jsonpath_match,
                            field,
                        )
                    )
            else:
                field = self.__get_field_name_from_rule_then(
                    jsonpath_match, rule.then
                )
                rule_function = globals().get(rule.then.function)
                diagnostics.append(
                    self.__run_function(
                        rule,
                        rule.then,
                        rule_function,
                        jsonpath_match,
                        field,
                    )
                )
        return diagnostics

    def validate(self):
        ruleset = Ruleset(self.ruleset_path, self.verbose)

        function_importer_service = FunctionImporterService(
            self.custom_functions_path, self.verbose
        )
        function_importer_service.import_functions()

        rules = ruleset.get_rules()

        function_validator = FunctionValidator(rules, globals())
        function_validator.validate_functions()

        resolve_contract = any(rule.resolved for rule in rules)

        document_data = self.__get_document_data(resolve_contract)
        try:
            diagnostics: List[Diagnostic] = []
            for rule in rules:
                jsonpath_matches = self.__get_jsonpath_matches_from_rule(
                    rule, document_data
                )
                diagnostics.extend(self.__process_rule(rule, jsonpath_matches))

            return DiagnosticCollection(diagnostics)

        except Exception as error:
            escaped_error = escape(str(error))
            Logger.error(
                LogMessage.FAIL_TO_VALIDATE_DOCUMENT.format(
                    document_path=self.document_path, error=escaped_error
                )
            )
