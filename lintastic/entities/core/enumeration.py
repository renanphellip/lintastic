from typing import List, Union

from pydantic import BaseModel


class EnumerationFunctionOptions(BaseModel):
    values: List[Union[str, int, float]]


class EnumerationRuleThen(BaseModel):
    field: str
    function: str = 'enumeration'
    function_options: EnumerationFunctionOptions
