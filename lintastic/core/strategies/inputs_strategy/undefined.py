from lintastic.core.entities.functions import (
    UndefinedFunctionInputs,
    UndefinedRuleThen,
)
from lintastic.core.entities.jsonpath_match import JSONPathMatch
from lintastic.core.interfaces.inputs_strategy import IInputsStrategy
from lintastic.core.utils.shared import get_field_name


class UndefinedInputsStrategy(IInputsStrategy):
    @staticmethod
    def get_inputs(
        rule_name: str,
        rule_then: UndefinedRuleThen,
        jsonpath_match: JSONPathMatch,
    ) -> UndefinedFunctionInputs:
        field = get_field_name(jsonpath_match.context, rule_then)
        return UndefinedFunctionInputs(
            rule_name=rule_name,
            context=jsonpath_match.context,
            target_value=jsonpath_match.target_value,
            field=field,
        )
