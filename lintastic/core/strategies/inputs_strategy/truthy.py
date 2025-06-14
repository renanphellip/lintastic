from lintastic.core.entities.functions import (
    TruthyFunctionInputs,
    TruthyRuleThen,
)
from lintastic.core.entities.jsonpath_match import JSONPathMatch
from lintastic.core.interfaces.inputs_strategy import IInputsStrategy
from lintastic.core.utils.shared import get_field_name


class TruthyInputsStrategy(IInputsStrategy):
    @staticmethod
    def get_inputs(
        rule_name: str,
        rule_then: TruthyRuleThen,
        jsonpath_match: JSONPathMatch,
    ) -> TruthyFunctionInputs:
        field = get_field_name(jsonpath_match.context, rule_then)
        return TruthyFunctionInputs(
            rule_name=rule_name,
            context=jsonpath_match.context,
            target_value=jsonpath_match.target_value,
            field=field,
        )
