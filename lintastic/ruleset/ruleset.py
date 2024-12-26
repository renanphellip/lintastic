import json
from typing import List

from pydantic import ValidationError

from lintastic.entities import Rule, SpectralRuleset
from lintastic.enums import LogMessage
from lintastic.readers import FileReaderService
from lintastic.utils import Logger

from .function_strategy_mapper import FunctionStrategyMapper
from .rule_factory import RuleFactory


class Ruleset:
    def __init__(self, ruleset_path: str, verbose=False):
        self.ruleset_path = ruleset_path
        self.verbose = verbose
        self.function_strategy_mapper = FunctionStrategyMapper()
        self.rule_factory = RuleFactory(self.function_strategy_mapper)
        self.file_reader_service = FileReaderService(self.verbose)
        self.ruleset = self.__read_and_validate_ruleset()

    def __read_and_validate_ruleset(self) -> SpectralRuleset:
        try:
            ruleset_data = self.file_reader_service.read_file(
                self.ruleset_path
            )
            return SpectralRuleset.model_validate(ruleset_data)
        except (ValidationError, ValueError) as e:
            errors = []
            for error in e.errors():
                errors.append({
                    'field': error.get('loc', ['unknown'])[0],
                    'error_message': error.get('msg', 'unknown error'),
                })
            formatted_error = json.dumps(errors, ensure_ascii=False)
            Logger.error(
                LogMessage.INVALID_RULESET_SCHEMA.format(error=formatted_error)
            )

    def get_rules(self) -> List[Rule]:
        return [
            self.rule_factory.create_rule(rule_name, spectral_rule)
            for rule_name, spectral_rule in self.ruleset.rules.items()
        ]
