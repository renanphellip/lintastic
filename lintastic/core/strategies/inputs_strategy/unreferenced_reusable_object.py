from lintastic.core.entities.functions import (
    UnreferencedReusableObjectFunctionInputs,
    UnreferencedReusableObjectRuleThen,
)
from lintastic.core.entities.jsonpath_match import JSONPathMatch
from lintastic.core.interfaces.inputs_strategy import IInputsStrategy


class UnreferencedReusableObjectInputsStrategy(IInputsStrategy):
    @staticmethod
    def get_inputs(
        rule_name: str,
        rule_then: UnreferencedReusableObjectRuleThen,
        jsonpath_match: JSONPathMatch,
    ) -> UnreferencedReusableObjectFunctionInputs:
        return UnreferencedReusableObjectFunctionInputs(
            rule_name=rule_name,
            context=jsonpath_match.context,
            target_value=jsonpath_match.target_value,
            options=rule_then.function_options,
        )
