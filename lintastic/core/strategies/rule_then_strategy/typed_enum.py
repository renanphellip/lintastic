from lintastic.core.entities.functions.typed_enum import (
    TypedEnumFunctionOptions,
    TypedEnumRuleThen,
)
from lintastic.core.entities.spectral import SpectralRuleThen
from lintastic.core.interfaces.rule_then_strategy import IRuleThenStrategy


class TypedEnumRuleThenStrategy(IRuleThenStrategy):
    @staticmethod
    def set_rule_then(spectral_rule_then: SpectralRuleThen, rule_name: str):
        return TypedEnumRuleThen(
            function_options=TypedEnumFunctionOptions(
                type=spectral_rule_then.functionOptions.get('type', ''),
                enum=spectral_rule_then.functionOptions.get('enum'),
            )
        )
