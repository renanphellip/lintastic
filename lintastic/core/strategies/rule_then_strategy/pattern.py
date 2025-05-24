from lintastic.core.entities.functions.pattern import (
    PatternFunctionOptions,
    PatternRuleThen,
)
from lintastic.core.entities.spectral import SpectralRuleThen
from lintastic.core.interfaces.rule_then_strategy import IRuleThenStrategy


class PatternRuleThenStrategy(IRuleThenStrategy):
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen, rule_name: str):
        match = spectral_rule_then.functionOptions.get('match', '')
        not_match = spectral_rule_then.functionOptions.get('notMatch', '')
        if not match and not not_match:
            raise ValueError(f'{rule_name} - at least one of the function options ' 'must be defined.')
        return PatternRuleThen(function_options=PatternFunctionOptions(match=match, not_match=not_match))
