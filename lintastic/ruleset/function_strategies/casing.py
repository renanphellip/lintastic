from lintastic.entities.functions.casing import (
    CasingFunctionOptions,
    CasingRuleThen,
)
from lintastic.entities.spectral import SpectralRuleThen


class CasingFunctionStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
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
