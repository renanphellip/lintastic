from typing import Union

from pydantic import BaseModel


class LengthFunctionOptions(BaseModel):
    max: Union[int, float] = -1
    min: Union[int, float] = -1


class LengthRuleThen(BaseModel):
    field: str
    function: str = 'length'
    function_options: LengthFunctionOptions
