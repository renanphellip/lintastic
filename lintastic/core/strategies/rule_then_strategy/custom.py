from lintastic.core.entities.functions.custom import CustomRuleThen
from lintastic.core.entities.spectral import SpectralRuleThen
from lintastic.core.interfaces.rule_then_strategy import IRuleThenStrategy


class CustomRuleThenStrategy(IRuleThenStrategy):
    @staticmethod
    def set_rule_then(spectral_rule_then: SpectralRuleThen, rule_name: str):
        rule_then = spectral_rule_then.model_dump()
        return CustomRuleThen(
            field=rule_then.get('field'),
            function=rule_then.get('function'),
            function_options=rule_then.get('functionOptions'),
        )
