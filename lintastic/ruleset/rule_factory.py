import sys
from typing import List, Union

from pydantic import ValidationError
from rich.console import Console
from rich.markup import escape

from .function_strategy_mapper import FunctionStrategyMapper
from ..entities import SpectralRuleThen, SpectralRule, Rule
from .function_strategies.function_strategy import FunctionStrategy

class RuleFactory:
    def __init__(self, function_strategy_mapper=FunctionStrategyMapper(), console=Console(highlight=False)):
        self.console = console
        self.function_strategy_mapper = function_strategy_mapper

    def __process_rule_then(
        self, rule_name: str, rule_then: Union[SpectralRuleThen, List[SpectralRuleThen]]
    ) -> Union[FunctionStrategy, List[FunctionStrategy]]:
        if isinstance(rule_then, list):
            list_classified_rule_then = []
            for item in rule_then:
                rule_strategy = self.function_strategy_mapper.get_strategy(item.function)
                list_classified_rule_then.append(rule_strategy.set_rule_then(item, rule_name))
            return list_classified_rule_then
        rule_strategy = self.function_strategy_mapper.get_strategy(rule_then.function)
        classified_rule_then = rule_strategy.set_rule_then(rule_then, rule_name)
        return classified_rule_then

    def create_rule(self, rule_name: str, spectral_rule: SpectralRule) -> Rule:
        try:
            rule_then = self.__process_rule_then(
                rule_name, spectral_rule.then
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
            self.console.print(
                '[red]'
                f'Rule name: {rule_name}\n'
                f'Exception: {escape(str(error))}'
                '[/red]'
            )
            sys.exit(1)
