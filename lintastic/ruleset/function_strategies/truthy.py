from ...entities.spectral import SpectralRuleThen
from ...entities.core.truthy import TruthyRuleThen

class TruthyFunctionStrategy:
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen):
        return TruthyRuleThen(
            field=spectral_rule_then.field,
        )
