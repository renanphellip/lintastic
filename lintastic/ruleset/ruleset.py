import sys
from typing import Any, Dict, List

from pydantic import ValidationError
from rich.console import Console
from rich.markup import escape

from .function_strategy_mapper import FunctionStrategyMapper

from ..file_reader.file_reader_service import FileReaderService
from .rule_factory import RuleFactory

from ..entities.core import *
from ..entities import SpectralRuleset, Rule
from .function_strategies import *


class Ruleset:
    def __init__(self, ruleset_path: str, verbose=False):
        self.ruleset_path = ruleset_path
        self.verbose = verbose
        self.console = Console(highlight=False)
        self.function_strategy_mapper = FunctionStrategyMapper()
        self.rule_factory = RuleFactory(self.console, self.function_strategy_mapper)
        self.ruleset = self.__read_and_validate_ruleset()
        self.rules = self.__create_rules()
    
    def __read_and_validate_ruleset(self) -> SpectralRuleset:
        try:
            ruleset_data: Dict[str, Any] = FileReaderService.read_file(
                self.ruleset_path, self.verbose
            )
            return SpectralRuleset.model_validate(ruleset_data)
        except (ValidationError, ValueError) as error:
            self.console.print(
                f'[red]Invalid ruleset schema: {escape(str(error))}[/red]'
            )
            sys.exit(1)
    
    def __create_rules(self) -> List[Rule]:
        return [
            self.rule_factory.create_rule(rule_name, spectral_rule)
            for rule_name, spectral_rule in self.ruleset.rules.items()
        ]
