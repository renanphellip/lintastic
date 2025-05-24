from lintastic.core.entities.functions.alphabetical import (
    AlphabeticalFunctionOptions,
    AlphabeticalRuleThen,
)
from lintastic.core.entities.spectral import SpectralRuleThen
from lintastic.core.interfaces.rule_then_strategy import IRuleThenStrategy


class AlphabeticalRuleThenStrategy(IRuleThenStrategy):
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen, rule_name: str):
        return AlphabeticalRuleThen(
            field=spectral_rule_then.field,
            function_options=AlphabeticalFunctionOptions(keyed_by=spectral_rule_then.functionOptions.get('keyedBy')),
        )
