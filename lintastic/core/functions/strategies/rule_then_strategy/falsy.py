from lintastic.core.entities.functions.falsy import FalsyRuleThen
from lintastic.core.entities.spectral import SpectralRuleThen


class FalsyRuleThenStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        return FalsyRuleThen(
            field=spectral_rule_then.field,
        )
