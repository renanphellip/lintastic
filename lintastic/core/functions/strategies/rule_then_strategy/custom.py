from lintastic.core.entities.functions.custom import CustomRuleThen
from lintastic.core.entities.spectral import SpectralRuleThen


class CustomRuleThenStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        rule_then = spectral_rule_then.model_dump()
        return CustomRuleThen(
            field=rule_then.get('field'),
            function=rule_then.get('function'),
            function_options=rule_then.get('functionOptions'),
        )
