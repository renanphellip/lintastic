from lintastic.core.entities.functions import (
    PatternFunctionInputs,
    PatternRuleThen,
)
from lintastic.core.entities.jsonpath_match import JSONPathMatch
from lintastic.core.interfaces.inputs_strategy import IInputsStrategy


class PatternInputsStrategy(IInputsStrategy):
    @staticmethod
    def get_inputs(
        rule_name: str,
        rule_then: PatternRuleThen,
        jsonpath_match: JSONPathMatch,
    ) -> PatternFunctionInputs:
        return PatternFunctionInputs(
            rule_name=rule_name,
            context=jsonpath_match.context,
            target_value=jsonpath_match.target_value,
            options=rule_then.function_options,
        )
