from lintastic.entities.functions.undefined import UndefinedRuleThen
from lintastic.entities.spectral import SpectralRuleThen


class UndefinedFunctionStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        return UndefinedRuleThen(
            field=spectral_rule_then.field,
        )
