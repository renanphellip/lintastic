from dataclasses import dataclass
from typing import Any, List

from pydantic import BaseModel

from lintastic.core.enums.core_function import CoreFunction


class XORFunctionOptions(BaseModel):
    properties: List[str]


class XORRuleThen(BaseModel):
    function: CoreFunction = CoreFunction.XOR
    function_options: XORFunctionOptions


@dataclass
class XORFunctionInputs:
    rule_name: str
    context: str
    target_value: Any
    options: XORFunctionOptions
    field = None
