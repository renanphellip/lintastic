from typing import Any, Dict, List

from lintastic.core.entities.rule import Rule
from lintastic.core.enums.log_message import LogMessage
from lintastic.core.interfaces.function_validator_service import IFunctionValidatorService
from lintastic.utils.logger import Logger


class FunctionValidatorService(IFunctionValidatorService):
    def __init__(self, globals: Dict[str, Any]):
        super().__init__(globals)

    def validate_functions(self, rules: List[Rule]) -> None:
        missing_functions: List[str] = []

        for rule in rules:
            if isinstance(rule.then, list):
                for item in rule.then:
                    if item.function not in self.globals:
                        missing_functions.append(item.function)
            elif rule.then.function not in self.globals:
                missing_functions.append(rule.then.function)

        unique_missing_functions = set(missing_functions)
        if unique_missing_functions:
            string_missing_functions = ', '.join(unique_missing_functions)
            Logger.error(LogMessage.RULESET_FUNCTIONS_NOT_FOUND.format(functions=string_missing_functions))
