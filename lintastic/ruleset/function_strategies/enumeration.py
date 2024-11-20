from ...entities.spectral import SpectralRuleThen
from ...entities.core.enumeration import EnumerationRuleThen, EnumerationFunctionOptions

class EnumerationFunctionStrategy:
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen):
        return EnumerationRuleThen(
            field=spectral_rule_then.field,
            function_options=EnumerationFunctionOptions(
                values=spectral_rule_then.functionOptions.get('values')
            ),
        )
