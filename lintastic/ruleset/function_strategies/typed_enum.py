from lintastic.entities.functions.typed_enum import (
    TypedEnumFunctionOptions,
    TypedEnumRuleThen,
)
from lintastic.entities.spectral import SpectralRuleThen


class TypedEnumFunctionStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        return TypedEnumRuleThen(
            function_options=TypedEnumFunctionOptions(
                type=spectral_rule_then.functionOptions.get('type', ''),
                enum=spectral_rule_then.functionOptions.get('enum'),
            )
        )
