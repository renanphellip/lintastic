from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel

from lintastic.core.enums.casing import CasingType
from lintastic.core.enums.core_function import CoreFunction


class CasingFunctionOptions(BaseModel):
    type: CasingType
    disallow_digits: bool = True
    separator_char: str = ''
    separator_allow_leading: bool = False


class CasingRuleThen(BaseModel):
    function: CoreFunction = CoreFunction.CASING
    function_options: CasingFunctionOptions


@dataclass
class CasingFunctionInputs:
    rule_name: str
    context: str
    target_value: Any
    options: CasingFunctionOptions
    field = None
