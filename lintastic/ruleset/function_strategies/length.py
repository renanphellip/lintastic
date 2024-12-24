from lintastic.entities.functions.length import (
    LengthFunctionOptions,
    LengthRuleThen,
)
from lintastic.entities.spectral import SpectralRuleThen


class LengthFunctionStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        length_max = spectral_rule_then.functionOptions.get('max', -1)
        length_min = spectral_rule_then.functionOptions.get('min', -1)
        if not length_max and not length_min:
            raise ValueError(
                f'{rule_name} - at least one of the function options '
                'must be defined.'
            )
        return LengthRuleThen(
            field=spectral_rule_then.field,
            function_options=LengthFunctionOptions(
                max=length_max, min=length_min
            ),
        )