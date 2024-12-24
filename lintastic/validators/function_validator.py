from typing import Dict, List

from lintastic.entities.rule import Rule
from lintastic.enums import LogMessage
from lintastic.utils.logger import Logger


class FunctionValidator:
    def __init__(self, rules: List[Rule], context: Dict = globals()):
        self.rules = rules
        self.context = context

    def validate_functions(self):
        missing_functions: List[str] = []

        for rule in self.rules:
            if isinstance(rule.then, list):
                for item in rule.then:
                    if item.function not in self.context:
                        missing_functions.append(item.function)
            elif rule.then.function not in self.context:
                missing_functions.append(rule.then.function)

        unique_missing_functions = set(missing_functions)
        if unique_missing_functions:
            string_missing_functions = ', '.join(unique_missing_functions)
            Logger.error(
                LogMessage.RULESET_FUNCTIONS_NOT_FOUND.format(
                    functions=string_missing_functions
                )
            )
