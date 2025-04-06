from dataclasses import dataclass
from typing import Any, List, Union

from pydantic import BaseModel

from lintastic.core.enums.core_function import CoreFunction


class EnumerationFunctionOptions(BaseModel):
    values: List[Union[str, int, float]]


class EnumerationRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.ENUMERATION
    function_options: EnumerationFunctionOptions


@dataclass
class EnumerationFunctionInputs:
    rule_name: str
    context: str
    target_value: Any
    options: EnumerationFunctionOptions
    field: str
