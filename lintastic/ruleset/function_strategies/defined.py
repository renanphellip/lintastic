from lintastic.entities.core.defined import DefinedRuleThen
from lintastic.entities.spectral import SpectralRuleThen


class DefinedFunctionStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        return DefinedRuleThen(
            field=spectral_rule_then.field,
        )
