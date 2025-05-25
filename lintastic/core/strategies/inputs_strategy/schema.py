from lintastic.core.entities.functions import (
    SchemaFunctionInputs,
    SchemaRuleThen,
)
from lintastic.core.entities.jsonpath_match import JSONPathMatch
from lintastic.core.utils.shared import get_field_name


class SchemaInputsStrategy:
    def get_inputs(
        self,
        rule_name: str,
        rule_then: SchemaRuleThen,
        jsonpath_match: JSONPathMatch,
    ) -> SchemaFunctionInputs:
        field = get_field_name(jsonpath_match.context, rule_then)
        return SchemaFunctionInputs(
            rule_name=rule_name,
            context=jsonpath_match.context,
            target_value=jsonpath_match.target_value,
            options=rule_then.function_options,
            field=field,
        )
