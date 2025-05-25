from typing import List, Union

from pydantic import BaseModel

from lintastic.core.enums.severity import Severity
from lintastic.core.utils.shared import (
    quote_unquoted_jsonpaths,
    transform_data_to_list,
)

from .functions import (
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


class Rule(BaseModel):
    name: str
    description: str
    message: Union[str, List[str]]
    documentation: Union[str, List[str]]
    severity: Severity
    resolved: bool
    given: Union[str, List[str]]
    then: Union[
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
        List[
            Union[
                DefinedRuleThen,
                FalsyRuleThen,
                TruthyRuleThen,
                UndefinedRuleThen,
            ]
        ],
    ]

    def model_post_init(self, __context):
        self.message = transform_data_to_list(self.message)
        self.documentation = transform_data_to_list(self.documentation)
        self.given = transform_data_to_list(self.given)
        self.given = [quote_unquoted_jsonpaths(jsonpath) for jsonpath in self.given]
