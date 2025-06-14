from lintastic.core.entities.functions.undefined import UndefinedRuleThen
from lintastic.core.entities.spectral import SpectralRuleThen
from lintastic.core.interfaces.rule_then_strategy import IRuleThenStrategy


class UndefinedRuleThenStrategy(IRuleThenStrategy):
    @staticmethod
    def set_rule_then(spectral_rule_then: SpectralRuleThen, rule_name: str):
        return UndefinedRuleThen(
            field=spectral_rule_then.field,
        )
