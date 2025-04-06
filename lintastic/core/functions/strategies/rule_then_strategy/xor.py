from lintastic.core.entities.functions.xor import (
    XORFunctionOptions,
    XORRuleThen,
)
from lintastic.core.entities.spectral import SpectralRuleThen


class XORRuleThenStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        return XORRuleThen(
            function_options=XORFunctionOptions(
                properties=spectral_rule_then.functionOptions.get('properties')
            )
        )
