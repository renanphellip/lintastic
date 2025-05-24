from lintastic.core.entities.functions.defined import DefinedRuleThen
from lintastic.core.entities.spectral import SpectralRuleThen
from lintastic.core.interfaces.rule_then_strategy import IRuleThenStrategy


class DefinedRuleThenStrategy(IRuleThenStrategy):
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen, rule_name: str):
        return DefinedRuleThen(
            field=spectral_rule_then.field,
        )
