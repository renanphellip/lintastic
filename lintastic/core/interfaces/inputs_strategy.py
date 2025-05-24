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
from lintastic.core.entities.jsonpath_match import JSONPathMatch
from lintastic.core.interfaces.function_inputs import IFunctionInputs


class IInputsStrategy(ABC):
    @abstractmethod
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
    ) -> IFunctionInputs:
        pass
