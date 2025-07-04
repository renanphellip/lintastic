from typing import List, Union

from pydantic import ValidationError
from rich.markup import escape

from lintastic.core.entities.functions.defined import DefinedRuleThen
from lintastic.core.entities.functions.falsy import FalsyRuleThen
from lintastic.core.entities.functions.truthy import TruthyRuleThen
from lintastic.core.entities.functions.undefined import UndefinedRuleThen
from lintastic.core.entities.rule import Rule
from lintastic.core.entities.spectral import SpectralRule, SpectralRuleThen
from lintastic.core.enums.log_message import LogMessage
from lintastic.core.interfaces.rule_factory import IRuleFactory
from lintastic.core.strategies.rule_then_strategy_mapper import RuleThenStrategyMapper
from lintastic.utils.logger import Logger


class RuleFactory(IRuleFactory):
    def __init__(self):
        self.function_strategy_mapper = RuleThenStrategyMapper()

    def create_rule(self, rule_name: str, spectral_rule: SpectralRule) -> Rule:
        try:
            rule_then = self._process_multiple_rule_then(rule_name, spectral_rule.then) if isinstance(spectral_rule.then, list) else self._process_single_rule_then(rule_name, spectral_rule.then)
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
            Logger.error(LogMessage.FAIL_TO_CREATE_RULE.format(rule_name=rule_name, error=escaped_error))

    def _process_multiple_rule_then(self, rule_name: str, rule_then: List[SpectralRuleThen]):
        list_classified_rule_then: List[
            Union[
                DefinedRuleThen,
                FalsyRuleThen,
                TruthyRuleThen,
                UndefinedRuleThen,
            ]
        ] = []
        for item in rule_then:
            rule_strategy = self.function_strategy_mapper.get_strategy(item.function)
            list_classified_rule_then.append(rule_strategy.set_rule_then(item, rule_name))
        return list_classified_rule_then

    def _process_single_rule_then(self, rule_name: str, rule_then: SpectralRuleThen):
        rule_strategy = self.function_strategy_mapper.get_strategy(rule_then.function)
        classified_rule_then = rule_strategy.set_rule_then(rule_then, rule_name)
        return classified_rule_then
