import json
from typing import Any, Callable, Dict, List, Union

from lintastic.core.entities.diagnostic import Diagnostic
from lintastic.core.entities.functions import (
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
from lintastic.core.entities.jsonpath_match import JSONPathMatch
from lintastic.core.entities.rule import Rule
from lintastic.core.enums.log_message import LogMessage
from lintastic.core.strategies.inputs_strategy_mapper import (
    InputsStrategyMapper,
)
from lintastic.core.interfaces.rule_processor_service import IRuleProcessorService
from lintastic.utils.logger import Logger


class RuleProcessorService(IRuleProcessorService):
    def __init__(self, globals: Dict[str, Any]):
        super().__init__(globals)

    def process(self, rule: Rule, jsonpath_matches: List[JSONPathMatch]) -> List[Diagnostic]:
        diagnostics: List[Diagnostic] = []
        for jsonpath_match in jsonpath_matches:
            then_statements = rule.then if isinstance(rule.then, list) else [rule.then]
            for rule_then in then_statements:
                rule_function = self.globals.get(rule_then.function)
                diagnostic = self._run_function(rule, rule_then, rule_function, jsonpath_match)
                if diagnostic:
                    diagnostics.append(diagnostic)
        return diagnostics

    def _run_function(
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
        inputs_strategy_mapper = InputsStrategyMapper()
        inputs_strategy = inputs_strategy_mapper.get_strategy(rule_then.function)
        function_inputs = inputs_strategy.get_inputs(rule.name, rule_then, jsonpath_match)

        rule_processing_data = {
            'rule': function_inputs.rule_name,
            'context': function_inputs.context,
            'function': rule_then.function,
        }
        if function_inputs.field:
            rule_processing_data['field'] = function_inputs.field
        if function_inputs.options:
            rule_processing_data['options'] = dict(function_inputs.options)
        rule_processing_data = json.dumps(rule_processing_data)
        Logger.debug(LogMessage.RUNNING_FUNCTION.format(rule_processing_data=rule_processing_data))

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
