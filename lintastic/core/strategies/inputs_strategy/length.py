from lintastic.core.entities.functions import (
    LengthFunctionInputs,
    LengthRuleThen,
)
from lintastic.core.entities.jsonpath_match import JSONPathMatch
from lintastic.core.utils.shared import get_field_name


class LengthInputsStrategy:
    def get_inputs(
        self,
        rule_name: str,
        rule_then: LengthRuleThen,
        jsonpath_match: JSONPathMatch,
    ) -> LengthFunctionInputs:
        field = get_field_name(jsonpath_match.context, rule_then)
        return LengthFunctionInputs(
            rule_name=rule_name,
            context=jsonpath_match.context,
            target_value=jsonpath_match.target_value,
            options=rule_then.function_options,
            field=field,
        )
