from typing import Any, Callable, Dict, List, Union

from rich.markup import escape

from lintastic.entities.diagnostic import Diagnostic
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
from lintastic.enums.log_message import LogMessage
from lintastic.utils.logger import Logger
from lintastic.validators.jsonpath_validator import JSONPathValidator


class RuleProcessor:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def get_jsonpath_matches(
        self, rule: Rule, document_data: Dict[str, Any]
    ) -> List[JSONPathMatch]:
        results = []
        for jsonpath in rule.given:
            results.extend(
                JSONPathValidator(
                    jsonpath, document_data, self.verbose
                ).validate()
            )
        return results

    @staticmethod
    def get_field_name(jsonpath_match: JSONPathMatch, rule_then: Any) -> str:
        return getattr(
            rule_then, 'field', jsonpath_match.context.split('.')[-1]
        )

    def run_function(
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
    ) -> Union[Diagnostic, None]:
        if self.verbose:
            Logger.debug(
                LogMessage.RUNNING_FUNCTION.format(
                    function_name=rule_then.function,
                    jsonpath_match=escape(str(jsonpath_match)),
                )
            )
        function_messages = rule_function(
            jsonpath_match.context,
            jsonpath_match.target_value,
            rule_then.function_options,
            field,
            self.verbose,
            rule.name,
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

    def process(
        self, rule: Rule, jsonpath_matches: List[JSONPathMatch]
    ) -> List[Diagnostic]:
        diagnostics: List[Diagnostic] = []
        for jsonpath_match in jsonpath_matches:
            then_statements = (
                rule.then if isinstance(rule.then, list) else [rule.then]
            )
            for rule_then in then_statements:
                field = self.get_field_name(jsonpath_match, rule_then)
                rule_function = globals().get(rule_then.function)
                diagnostic = self.run_function(
                    rule, rule_then, rule_function, jsonpath_match, field
                )
                if diagnostic:
                    diagnostics.append(diagnostic)
        return diagnostics
