from ...entities.spectral import SpectralRuleThen
from ...entities.core.typed_enum import TypedEnumRuleThen, TypedEnumFunctionOptions

class TypedEnumFunctionStrategy:
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen):
        return TypedEnumRuleThen(
            function_options=TypedEnumFunctionOptions(
                type=spectral_rule_then.functionOptions.get('type', ''),
                enum=spectral_rule_then.functionOptions.get('enum'),
            )
        )
