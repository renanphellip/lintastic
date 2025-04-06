from lintastic.core.entities.functions.enumeration import (
    EnumerationFunctionOptions,
    EnumerationRuleThen,
)
from lintastic.core.entities.spectral import SpectralRuleThen


class EnumerationRuleThenStrategy:
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
