from typing import Protocol

from ...entities.spectral import SpectralRuleThen

class FunctionStrategy(Protocol):
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen, rule_name: str = None): ...
