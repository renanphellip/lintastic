from lintastic.core.entities.functions import (
    DefinedFunctionInputs,
    DefinedRuleThen,
)
from lintastic.core.entities.jsonpath_match import JSONPathMatch
from lintastic.core.utils.shared import get_field_name


class DefinedInputsStrategy:
    def get_inputs(
        self,
        rule_name: str,
        rule_then: DefinedRuleThen,
        jsonpath_match: JSONPathMatch,
    ) -> DefinedFunctionInputs:
        field = get_field_name(jsonpath_match.context, rule_then)
        return DefinedFunctionInputs(
            rule_name=rule_name,
            context=jsonpath_match.context,
            target_value=jsonpath_match.target_value,
            field=field,
        )
