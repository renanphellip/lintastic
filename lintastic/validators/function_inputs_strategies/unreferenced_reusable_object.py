from lintastic.entities.functions import (
    UnreferencedReusableObjectRuleThen
)
from lintastic.entities.functions.inputs import FunctionInputs
from lintastic.entities.jsonpath import JSONPathMatch
from lintastic.entities.rule import Rule


class UnreferencedReusableObjectInputsStrategy():
    # ruff: noqa: PLR6301
    def get_inputs(
        self,
        rule_name: str,
        rule_then: UnreferencedReusableObjectRuleThen,
        jsonpath_match: JSONPathMatch,
        verbose: bool
    ) -> FunctionInputs:
        return FunctionInputs(
            rule_name=rule_name,
            context=jsonpath_match.context,
            target_value=jsonpath_match.target_value,
            options=rule_then.function_options,
            verbose=verbose
        )
