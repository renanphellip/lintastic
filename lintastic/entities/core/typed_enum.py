from typing import List, Union

from pydantic import BaseModel


class TypedEnumFunctionOptions(BaseModel):
    type: str = ''
    enum: Union[List[str], List[int], List[float]]


class TypedEnumRuleThen(BaseModel):
    function: str = 'typedEnum'
    function_options: TypedEnumFunctionOptions
