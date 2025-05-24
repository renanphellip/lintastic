from lintastic.core.entities.functions.truthy import TruthyRuleThen
from lintastic.core.entities.spectral import SpectralRuleThen
from lintastic.core.interfaces.rule_then_strategy import IRuleThenStrategy


class TruthyRuleThenStrategy(IRuleThenStrategy):
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen, rule_name: str):
        return TruthyRuleThen(
            field=spectral_rule_then.field,
        )
