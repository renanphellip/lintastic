from typing import Any, Dict, List

from lintastic.core.entities.rule import Rule
from lintastic.core.enums.log_message import LogMessage
from lintastic.utils.logger import Logger


class FunctionValidator:
    def __init__(self, rules: List[Rule], globals: Dict[str, Any] = globals()):
        self.rules = rules
        self.globals = globals

    def validate_functions(self) -> None:
        missing_functions: List[str] = []

        for rule in self.rules:
            if isinstance(rule.then, list):
                for item in rule.then:
                    if item.function not in self.globals:
                        missing_functions.append(item.function)
            elif rule.then.function not in self.globals:
                missing_functions.append(rule.then.function)

        unique_missing_functions = set(missing_functions)
        if unique_missing_functions:
            string_missing_functions = ', '.join(unique_missing_functions)
            Logger.error(
                LogMessage.RULESET_FUNCTIONS_NOT_FOUND.format(
                    functions=string_missing_functions
                )
            )
