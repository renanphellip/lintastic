from typing import List, Union

from pydantic import BaseModel

from lintastic.enums import CoreFunction


class TypedEnumFunctionOptions(BaseModel):
    type: str = ''
    enum: Union[List[str], List[int], List[float]]


class TypedEnumRuleThen(BaseModel):
    function: CoreFunction = CoreFunction.TYPED_ENUM
    function_options: TypedEnumFunctionOptions
