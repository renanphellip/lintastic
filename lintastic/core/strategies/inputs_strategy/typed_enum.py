from lintastic.core.entities.functions import (
    TypedEnumFunctionInputs,
    TypedEnumRuleThen,
)
from lintastic.core.entities.jsonpath_match import JSONPathMatch


class TypedEnumInputsStrategy:
    def get_inputs(
        self,
        rule_name: str,
        rule_then: TypedEnumRuleThen,
        jsonpath_match: JSONPathMatch,
    ) -> TypedEnumFunctionInputs:
        return TypedEnumFunctionInputs(
            rule_name=rule_name,
            context=jsonpath_match.context,
            target_value=jsonpath_match.target_value,
            options=rule_then.function_options,
        )
