from lintastic.core.entities.functions import (
    AlphabeticalFunctionInputs,
    AlphabeticalRuleThen,
)
from lintastic.core.entities.jsonpath_match import JSONPathMatch
from lintastic.core.interfaces.inputs_strategy import IInputsStrategy
from lintastic.core.utils.shared import get_field_name


class AlphabeticalInputsStrategy(IInputsStrategy):
    @staticmethod
    def get_inputs(
        rule_name: str,
        rule_then: AlphabeticalRuleThen,
        jsonpath_match: JSONPathMatch,
    ) -> AlphabeticalFunctionInputs:
        field = get_field_name(jsonpath_match.context, rule_then)
        return AlphabeticalFunctionInputs(
            rule_name=rule_name,
            context=jsonpath_match.context,
            target_value=jsonpath_match.target_value,
            options=rule_then.function_options,
            field=field,
        )
