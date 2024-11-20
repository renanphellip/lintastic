from ...entities.spectral import SpectralRuleThen
from ...entities.custom import CustomRuleThen

class CustomFunctionStrategy:
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen):
        return CustomRuleThen(**spectral_rule_then.model_dump())
