from typing import Protocol

from lintastic.entities.spectral import SpectralRuleThen


class FunctionStrategy(Protocol):
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str = None
    ): ...
