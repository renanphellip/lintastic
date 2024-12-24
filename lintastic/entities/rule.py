from typing import List, Union

from pydantic import BaseModel

from lintastic.enums import Severity

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

    @staticmethod
    def _quote_unquoted_jsonpaths(jsonpath: str) -> str:
        paths = jsonpath.split('.')
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

    @staticmethod
    def _transform_data_to_list(data: str) -> List[str]:
        return data if isinstance(data, list) else [data] if data else []

    def model_post_init(self, __context):
        self.message = self._transform_data_to_list(self.message)
        self.documentation = self._transform_data_to_list(self.documentation)
        self.given = self._transform_data_to_list(self.given)
        self.given = [
            self._quote_unquoted_jsonpaths(jsonpath) for jsonpath in self.given
        ]
