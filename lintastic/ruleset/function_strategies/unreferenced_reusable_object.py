from lintastic.entities.functions.unreferenced_reusable_object import (
    UnreferencedReusableObjectFunctionOptions,
    UnreferencedReusableObjectRuleThen,
)
from lintastic.entities.spectral import SpectralRuleThen


class UnreferencedReusableObjectFunctionStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        return UnreferencedReusableObjectRuleThen(
            function_options=UnreferencedReusableObjectFunctionOptions(
                reusable_objects_location=spectral_rule_then.functionOptions.get(
                    'reusableObjectsLocation'
                )
            )
        )
