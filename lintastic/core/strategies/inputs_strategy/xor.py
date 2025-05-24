from lintastic.core.entities.functions import XORFunctionInputs, XORRuleThen
from lintastic.core.entities.jsonpath_match import JSONPathMatch


class XORInputsStrategy:
    def get_inputs(
        self,
        rule_name: str,
        rule_then: XORRuleThen,
        jsonpath_match: JSONPathMatch,
    ) -> XORFunctionInputs:
        return XORFunctionInputs(
            rule_name=rule_name,
            context=jsonpath_match.context,
            target_value=jsonpath_match.target_value,
            options=rule_then.function_options,
        )
