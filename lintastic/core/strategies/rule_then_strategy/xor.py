from lintastic.core.entities.functions.xor import (
    XORFunctionOptions,
    XORRuleThen,
)
from lintastic.core.entities.spectral import SpectralRuleThen
from lintastic.core.interfaces.rule_then_strategy import IRuleThenStrategy


class XORRuleThenStrategy(IRuleThenStrategy):
    @staticmethod
    def set_rule_then(spectral_rule_then: SpectralRuleThen, rule_name: str):
        return XORRuleThen(function_options=XORFunctionOptions(properties=spectral_rule_then.functionOptions.get('properties')))
