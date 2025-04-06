from lintastic.core.entities.functions import (
    EnumerationFunctionInputs,
    EnumerationRuleThen,
)
from lintastic.core.entities.jsonpath import JSONPathMatch
from lintastic.utils.shared import get_field_name_from_jsonpath_context


class EnumerationInputsStrategy:
    # ruff: noqa: PLR6301
    def get_inputs(
        self,
        rule_name: str,
        rule_then: EnumerationRuleThen,
        jsonpath_match: JSONPathMatch,
    ) -> EnumerationFunctionInputs:
        field = get_field_name_from_jsonpath_context(
            jsonpath_match.context, rule_then
        )
        return EnumerationFunctionInputs(
            rule_name=rule_name,
            context=jsonpath_match.context,
            target_value=jsonpath_match.target_value,
            options=rule_then.function_options,
            field=field,
        )
