from ...entities.spectral import SpectralRuleThen
from ...entities.core.defined import DefinedRuleThen

class DefinedFunctionStrategy:
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen):
        return DefinedRuleThen(
            field=spectral_rule_then.field,
        )
