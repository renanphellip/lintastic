from abc import ABC, abstractmethod
from typing import Union

from lintastic.core.entities.functions import (
    AlphabeticalRuleThen,
    CasingRuleThen,
    CustomRuleThen,
    DefinedRuleThen,
    EnumerationRuleThen,
    FalsyRuleThen,
    LengthRuleThen,
    PatternRuleThen,
    SchemaRuleThen,
    TruthyRuleThen,
    TypedEnumRuleThen,
    UndefinedRuleThen,
    UnreferencedReusableObjectRuleThen,
    XORRuleThen,
)
from lintastic.core.entities.spectral import SpectralRuleThen


class IRuleThenStrategy(ABC):
    @abstractmethod
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ) -> Union[
        AlphabeticalRuleThen,
        CasingRuleThen,
        CustomRuleThen,
        DefinedRuleThen,
        EnumerationRuleThen,
        FalsyRuleThen,
        LengthRuleThen,
        PatternRuleThen,
        SchemaRuleThen,
        TruthyRuleThen,
        TypedEnumRuleThen,
        UndefinedRuleThen,
        UnreferencedReusableObjectRuleThen,
        XORRuleThen,
    ]:
        pass
