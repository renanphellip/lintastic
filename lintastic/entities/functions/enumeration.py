from typing import List, Union

from pydantic import BaseModel

from lintastic.enums import CoreFunction


class EnumerationFunctionOptions(BaseModel):
    values: List[Union[str, int, float]]


class EnumerationRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.ENUMERATION
    function_options: EnumerationFunctionOptions
