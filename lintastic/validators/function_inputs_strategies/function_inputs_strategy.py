from typing import Protocol, Union

from lintastic.entities.diagnostic import Diagnostic
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
from lintastic.entities.functions.inputs import FunctionInputs
from lintastic.entities.jsonpath import JSONPathMatch
from lintastic.entities.rule import Rule
from lintastic.entities.spectral import SpectralRuleThen


class FunctionInputsStrategy(Protocol):
    # ruff: noqa: PLR6301
    def get_inputs(
        self,
        rule_name: str,
        rule_then: Union[
            AlphabeticalRuleThen,
            CasingRuleThen,
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
            CustomRuleThen,
        ],
        jsonpath_match: JSONPathMatch,
        verbose: bool
    ) -> FunctionInputs: ...
