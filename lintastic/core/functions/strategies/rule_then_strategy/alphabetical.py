from lintastic.core.entities.functions.alphabetical import (
    AlphabeticalFunctionOptions,
    AlphabeticalRuleThen,
)
from lintastic.core.entities.spectral import SpectralRuleThen


class AlphabeticalRuleThenStrategy:
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
