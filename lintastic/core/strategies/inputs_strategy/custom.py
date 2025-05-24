from lintastic.core.entities.functions import (
    CustomFunctionInputs,
    CustomRuleThen,
)
from lintastic.core.entities.jsonpath_match import JSONPathMatch
from lintastic.utils.shared import get_field_name


class CustomInputsStrategy:
    # ruff: noqa: PLR6301
    def get_inputs(
        self,
        rule_name: str,
        rule_then: CustomRuleThen,
        jsonpath_match: JSONPathMatch,
    ) -> CustomFunctionInputs:
        field = get_field_name(jsonpath_match.context, rule_then)
        return CustomFunctionInputs(
            rule_name=rule_name,
            context=jsonpath_match.context,
            target_value=jsonpath_match.target_value,
            options=rule_then.function_options,
            field=field,
        )
