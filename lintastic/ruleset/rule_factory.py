from typing import List

from pydantic import ValidationError
from rich.markup import escape

from lintastic.entities import Rule, SpectralRule, SpectralRuleThen
from lintastic.enums import LogMessage
from lintastic.utils.logger import Logger

from .function_strategies.function_strategy import FunctionStrategy
from .function_strategy_mapper import FunctionStrategyMapper


class RuleFactory:
    def __init__(self, function_strategy_mapper=FunctionStrategyMapper()):
        self.function_strategy_mapper = function_strategy_mapper

    def __process_single_rule_then(
        self, rule_name: str, rule_then: SpectralRuleThen
    ) -> FunctionStrategy:
        rule_strategy = self.function_strategy_mapper.get_strategy(
            rule_then.function
        )
        classified_rule_then = rule_strategy.set_rule_then(
            rule_then, rule_name
        )
        return classified_rule_then

    def __process_multiple_rule_then(
        self, rule_name: str, rule_then: List[SpectralRuleThen]
    ) -> List[FunctionStrategy]:
        list_classified_rule_then: List[FunctionStrategy] = []
        for item in rule_then:
            rule_strategy = self.function_strategy_mapper.get_strategy(
                item.function
            )
            list_classified_rule_then.append(
                rule_strategy.set_rule_then(item, rule_name)
            )
        return list_classified_rule_then

    def create_rule(self, rule_name: str, spectral_rule: SpectralRule) -> Rule:
        try:
            rule_then = (
                self.__process_multiple_rule_then(
                    rule_name, spectral_rule.then
                )
                if isinstance(spectral_rule.then, list)
                else self.__process_single_rule_then(
                    rule_name, spectral_rule.then
                )
            )
            return Rule(
                name=rule_name,
                description=spectral_rule.description,
                message=spectral_rule.message,
                documentation=spectral_rule.documentation,
                severity=spectral_rule.severity,
                resolved=spectral_rule.resolved,
                given=spectral_rule.given,
                then=rule_then,
            )
        except (ValidationError, ValueError) as error:
            escaped_error = escape(str(error))
            Logger.error(
                LogMessage.FAIL_TO_CREATE_RULE.format(
                    rule_name=rule_name, error=escaped_error
                )
            )
