from lintastic.core.entities.functions.undefined import UndefinedRuleThen
from lintastic.core.entities.spectral import SpectralRuleThen


class UndefinedRuleThenStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        return UndefinedRuleThen(
            field=spectral_rule_then.field,
        )
