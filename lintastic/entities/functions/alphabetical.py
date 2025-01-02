from pydantic import BaseModel

from lintastic.enums.core_function import CoreFunction


class AlphabeticalFunctionOptions(BaseModel):
    keyed_by: str


class AlphabeticalRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.ALPHABETICAL
    function_options: AlphabeticalFunctionOptions
