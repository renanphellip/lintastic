from typing import Union

from pydantic import BaseModel

from lintastic.enums.core_function import CoreFunction


class LengthFunctionOptions(BaseModel):
    max: Union[int, float] = -1
    min: Union[int, float] = -1


class LengthRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.LENGTH
    function_options: LengthFunctionOptions
