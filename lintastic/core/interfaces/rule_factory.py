from abc import ABC, abstractmethod

from lintastic.core.entities.rule import Rule
from lintastic.core.entities.spectral import SpectralRule


class IRuleFactory(ABC):
    @abstractmethod
    def create_rule(self, rule_name: str, spectral_rule: SpectralRule) -> Rule:
        pass
