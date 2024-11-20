from ...entities.spectral import SpectralRuleThen
from ...entities.core.casing import CasingRuleThen, CasingFunctionOptions

class CasingFunctionStrategy:
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen):
        return CasingRuleThen(
            function_options=CasingFunctionOptions(
                type=spectral_rule_then.functionOptions.get('type'),
                disallow_digits=spectral_rule_then.functionOptions.get(
                    'disallowDigits', True
                ),
                separator_char=spectral_rule_then.functionOptions.get(
                    'separator.char', ''
                ),
                separator_allow_leading=spectral_rule_then.functionOptions.get(
                    'separator.allowLeading', False
                ),
            )
        )
