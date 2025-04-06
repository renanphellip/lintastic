from lintastic.core.entities.functions import (
    UndefinedFunctionInputs,
    UndefinedRuleThen,
)
from lintastic.core.entities.jsonpath import JSONPathMatch
from lintastic.utils.shared import get_field_name_from_jsonpath_context


class UndefinedInputsStrategy:
    # ruff: noqa: PLR6301
    def get_inputs(
        self,
        rule_name: str,
        rule_then: UndefinedRuleThen,
        jsonpath_match: JSONPathMatch,
        verbose: bool,
    ) -> UndefinedFunctionInputs:
        field = get_field_name_from_jsonpath_context(
            jsonpath_match.context, rule_then
        )
        return UndefinedFunctionInputs(
            rule_name=rule_name,
            context=jsonpath_match.context,
            target_value=jsonpath_match.target_value,
            field=field,
            verbose=verbose,
        )
