from dataclasses import dataclass
from typing import Any, Union

from pydantic import BaseModel

from lintastic.core.enums.core_function import CoreFunction


class LengthFunctionOptions(BaseModel):
    max: Union[int, float] = -1
    min: Union[int, float] = -1


class LengthRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.LENGTH
    function_options: LengthFunctionOptions


@dataclass
class LengthFunctionInputs:
    rule_name: str
    context: str
    target_value: Any
    options: LengthFunctionOptions
    field: str
    verbose: bool = False
