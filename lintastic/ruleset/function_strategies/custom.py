from lintastic.entities.custom import CustomRuleThen
from lintastic.entities.spectral import SpectralRuleThen


class CustomFunctionStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        return CustomRuleThen(**spectral_rule_then.model_dump())
