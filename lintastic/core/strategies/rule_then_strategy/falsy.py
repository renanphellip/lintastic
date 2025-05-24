from lintastic.core.entities.functions.falsy import FalsyRuleThen
from lintastic.core.entities.spectral import SpectralRuleThen
from lintastic.core.interfaces.rule_then_strategy import IRuleThenStrategy


class FalsyRuleThenStrategy(IRuleThenStrategy):
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen, rule_name: str):
        return FalsyRuleThen(
            field=spectral_rule_then.field,
        )
