from ...entities.spectral import SpectralRuleThen
from ...entities.core.xor import XORRuleThen, XORFunctionOptions

class XORFunctionStrategy:
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen):
        return XORRuleThen(
            function_options=XORFunctionOptions(
                properties=spectral_rule_then.functionOptions.get('properties')
            )
        )
