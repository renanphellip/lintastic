from lintastic.core.entities.functions import (
    TruthyFunctionInputs,
    TruthyRuleThen,
)
from lintastic.core.entities.jsonpath import JSONPathMatch
from lintastic.utils.shared import get_field_name_from_jsonpath_context


class TruthyInputsStrategy:
    # ruff: noqa: PLR6301
    def get_inputs(
        self,
        rule_name: str,
        rule_then: TruthyRuleThen,
        jsonpath_match: JSONPathMatch,
        verbose: bool,
    ) -> TruthyFunctionInputs:
        field = get_field_name_from_jsonpath_context(
            jsonpath_match.context, rule_then
        )
        return TruthyFunctionInputs(
            rule_name=rule_name,
            context=jsonpath_match.context,
            target_value=jsonpath_match.target_value,
            field=field,
            verbose=verbose,
        )
