from ...entities.spectral import SpectralRuleThen
from ...entities.core.falsy import FalsyRuleThen

class FalsyFunctionStrategy:
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen):
        return FalsyRuleThen(
            field=spectral_rule_then.field,
        )