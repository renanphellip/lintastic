from lintastic.entities.functions.alphabetical import (
    AlphabeticalFunctionOptions,
    AlphabeticalRuleThen,
)
from lintastic.entities.spectral import SpectralRuleThen


class AlphabeticalFunctionStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        return AlphabeticalRuleThen(
            field=spectral_rule_then.field,
            function_options=AlphabeticalFunctionOptions(
                keyed_by=spectral_rule_then.functionOptions.get('keyedBy')
            ),
        )