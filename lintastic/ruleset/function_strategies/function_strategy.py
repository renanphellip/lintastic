from typing import Protocol, Union

from lintastic.entities.functions import (
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
from lintastic.entities.spectral import SpectralRuleThen


class FunctionStrategy(Protocol):
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str = None
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
    ]: ...
