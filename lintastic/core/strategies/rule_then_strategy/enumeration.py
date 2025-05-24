from lintastic.core.entities.functions.enumeration import (
    EnumerationFunctionOptions,
    EnumerationRuleThen,
)
from lintastic.core.entities.spectral import SpectralRuleThen
from lintastic.core.interfaces.rule_then_strategy import IRuleThenStrategy


class EnumerationRuleThenStrategy(IRuleThenStrategy):
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen, rule_name: str):
        return EnumerationRuleThen(
            field=spectral_rule_then.field,
            function_options=EnumerationFunctionOptions(values=spectral_rule_then.functionOptions.get('values')),
        )
