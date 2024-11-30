from lintastic.entities.core.truthy import TruthyRuleThen
from lintastic.entities.spectral import SpectralRuleThen


class TruthyFunctionStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        return TruthyRuleThen(
            field=spectral_rule_then.field,
        )
