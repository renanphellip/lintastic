from lintastic.core.entities.functions.truthy import TruthyRuleThen
from lintastic.core.entities.spectral import SpectralRuleThen


class TruthyRuleThenStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        return TruthyRuleThen(
            field=spectral_rule_then.field,
        )
