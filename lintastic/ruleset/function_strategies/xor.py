from lintastic.entities.functions.xor import (
    XORFunctionOptions,
    XORRuleThen,
)
from lintastic.entities.spectral import SpectralRuleThen


class XORFunctionStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        return XORRuleThen(
            function_options=XORFunctionOptions(
                properties=spectral_rule_then.functionOptions.get('properties')
            )
        )
