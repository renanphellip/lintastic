from ...entities.spectral import SpectralRuleThen
from ...entities.core.undefined import UndefinedRuleThen

class UndefinedFunctionStrategy:
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen):
        return UndefinedRuleThen(
            field=spectral_rule_then.field,
        )
