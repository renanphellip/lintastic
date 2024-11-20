from ...entities.spectral import SpectralRuleThen
from ...entities.core.alphabetical import AlphabeticalRuleThen, AlphabeticalFunctionOptions

class AlphabeticalFunctionStrategy:
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen):
        return AlphabeticalRuleThen(
            field=spectral_rule_then.field,
            function_options=AlphabeticalFunctionOptions(
                keyed_by=spectral_rule_then.functionOptions.get('keyedBy')
            ),
        )
