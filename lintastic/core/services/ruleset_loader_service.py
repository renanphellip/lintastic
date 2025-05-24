import json
from typing import List

from pydantic import ValidationError

from lintastic.core.entities.rule import Rule
from lintastic.core.entities.spectral import SpectralRuleset
from lintastic.core.enums.log_message import LogMessage
from lintastic.core.interfaces.rule_factory import IRuleFactory
from lintastic.io.interfaces.file_reader_service import IFileReaderService
from lintastic.utils.logger import Logger


class RulesetLoaderService:
    def __init__(self, file_reader_service: IFileReaderService, rule_factory: IRuleFactory):
        self.file_reader_service = file_reader_service
        self.rule_factory = rule_factory

    def get_rules(self) -> List[Rule]:
        rules = []
        for rule_name, spectral_rule in self.spectral_ruleset.rules.items():
            rules.append(self.rule_factory.create_rule(rule_name, spectral_rule))
        return rules

    def load_ruleset(self, ruleset_path: str) -> SpectralRuleset:
        try:
            ruleset_data = self.file_reader_service.read_file(ruleset_path)
            self.spectral_ruleset = SpectralRuleset.model_validate(ruleset_data)
            return self.spectral_ruleset
        except (ValidationError, ValueError) as e:
            errors = []
            for error in e.errors():
                errors.append({
                    'field': error.get('loc', ['unknown'])[0],
                    'error_message': error.get('msg', 'unknown error'),
                })
            formatted_error = json.dumps(errors, ensure_ascii=False)
            Logger.error(LogMessage.INVALID_RULESET_SCHEMA.format(error=formatted_error))
