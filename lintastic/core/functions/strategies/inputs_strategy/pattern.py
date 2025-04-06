from lintastic.core.entities.functions import (
    PatternFunctionInputs,
    PatternRuleThen,
)
from lintastic.core.entities.jsonpath import JSONPathMatch


class PatternInputsStrategy:
    # ruff: noqa: PLR6301
    def get_inputs(
        self,
        rule_name: str,
        rule_then: PatternRuleThen,
        jsonpath_match: JSONPathMatch,
    ) -> PatternFunctionInputs:
        return PatternFunctionInputs(
            rule_name=rule_name,
            context=jsonpath_match.context,
            target_value=jsonpath_match.target_value,
            options=rule_then.function_options,
        )
