from dataclasses import dataclass
from typing import Any, List, Union

from pydantic import BaseModel

from lintastic.core.enums.core_function import CoreFunction


class TypedEnumFunctionOptions(BaseModel):
    type: str = ''
    enum: Union[List[str], List[int], List[float]]


class TypedEnumRuleThen(BaseModel):
    function: CoreFunction = CoreFunction.TYPED_ENUM
    function_options: TypedEnumFunctionOptions


@dataclass
class TypedEnumFunctionInputs:
    rule_name: str
    context: str
    target_value: Any
    options: TypedEnumFunctionOptions
    field = None
    verbose: bool = False
