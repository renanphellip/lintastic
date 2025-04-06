from typing import Protocol, Union

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
from lintastic.core.entities.functions.function import FunctionInputs
from lintastic.core.entities.jsonpath import JSONPathMatch


class InputsStrategy(Protocol):
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
    ) -> FunctionInputs: ...
