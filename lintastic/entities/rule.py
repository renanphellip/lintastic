from typing import List, Union

from pydantic import BaseModel

from .core import (
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
    XORRuleThen
)
from .spectral import Severity
from .custom import CustomRuleThen


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

    @staticmethod
    def __process_given(given_string: str) -> str:
        paths = given_string.split('.')
        processed_paths = []
        for path in paths:
            if (
                '/' in path
                and not path.startswith(('"', "'"))
                and not path.endswith(('"', "'"))
            ):
                processed_paths.append(f'"{path}"')
            else:
                processed_paths.append(path)
        return '.'.join(processed_paths)

    def model_post_init(self, __context):
        self.message = (
            self.message
            if isinstance(self.message, list)
            else [self.message]
            if self.message
            else []
        )
        self.documentation = (
            self.documentation
            if isinstance(self.documentation, list)
            else [self.documentation]
            if self.documentation
            else []
        )
        self.given = (
            [self.__process_given(context) for context in self.given]
            if isinstance(self.given, list)
            else [self.given]
            if self.given
            else []
        )
