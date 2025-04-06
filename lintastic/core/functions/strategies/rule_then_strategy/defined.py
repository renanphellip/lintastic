from lintastic.core.entities.functions.defined import DefinedRuleThen
from lintastic.core.entities.spectral import SpectralRuleThen


class DefinedRuleThenStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        return DefinedRuleThen(
            field=spectral_rule_then.field,
        )
