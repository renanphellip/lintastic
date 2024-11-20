from ...entities.spectral import SpectralRuleThen
from ...entities.core.unreferenced_reusable_object import UnreferencedReusableObjectRuleThen, UnreferencedReusableObjectFunctionOptions

class UnreferencedReusableObjectFunctionStrategy:
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen):
        return UnreferencedReusableObjectRuleThen(
            function_options=UnreferencedReusableObjectFunctionOptions(
                reusable_objects_location=spectral_rule_then.functionOptions.get(
                    'reusableObjectsLocation'
                )
            )
        )
