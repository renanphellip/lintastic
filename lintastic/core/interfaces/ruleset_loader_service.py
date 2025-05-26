from abc import ABC, abstractmethod
from typing import List

from lintastic.core.entities.rule import Rule
from lintastic.core.entities.spectral import SpectralRuleset
from lintastic.core.interfaces.rule_factory import IRuleFactory
from lintastic.io.interfaces.file_reader_service import IFileReaderService


class IRulesetLoaderService(ABC):
    def __init__(self, file_reader_service: IFileReaderService, rule_factory: IRuleFactory):
        self.file_reader_service = file_reader_service
        self.rule_factory = rule_factory

    @abstractmethod
    def load_ruleset(self, ruleset_path: str) -> SpectralRuleset:
        pass

    @abstractmethod
    def get_rules(self) -> List[Rule]:
        pass
