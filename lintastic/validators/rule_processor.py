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
from lintastic.validators.inputs_strategy_mapper import InputsStrategyMapper
from lintastic.validators.jsonpath_validator import JSONPathValidator


class RuleProcessor:
    def __init__(self, globals: Dict[str, Any], verbose=False):
        self.globals = globals
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
    ) -> Union[Diagnostic, None]:
        if self.verbose:
            Logger.debug(
                LogMessage.RUNNING_FUNCTION.format(
                    function_name=rule_then.function,
                    jsonpath_match=escape(str(jsonpath_match)),
                )
            )
        
        inputs_strategy_mapper = InputsStrategyMapper()
        inputs_strategy = inputs_strategy_mapper.get_strategy(rule_then.function)
        function_inputs = inputs_strategy.get_inputs(
            rule.name,
            rule.then,
            jsonpath_match,
            self.verbose
        )
        
        function_messages = rule_function(function_inputs)
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
                rule_function = self.globals.get(rule_then.function)
                diagnostic = self.run_function(
                    rule, rule_then, rule_function, jsonpath_match
                )
                if diagnostic:
                    diagnostics.append(diagnostic)
        return diagnostics
