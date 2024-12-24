from pydantic import BaseModel

from lintastic.enums import CoreFunction


class AlphabeticalFunctionOptions(BaseModel):
    keyed_by: str


class AlphabeticalRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.ALPHABETICAL
    function_options: AlphabeticalFunctionOptions
