from lintastic.entities.core.enumeration import (
    EnumerationFunctionOptions,
    EnumerationRuleThen,
)
from lintastic.entities.spectral import SpectralRuleThen


class EnumerationFunctionStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        return EnumerationRuleThen(
            field=spectral_rule_then.field,
            function_options=EnumerationFunctionOptions(
                values=spectral_rule_then.functionOptions.get('values')
            ),
        )
