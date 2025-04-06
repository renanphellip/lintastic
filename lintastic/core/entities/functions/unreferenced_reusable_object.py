from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel

from lintastic.core.enums.core_function import CoreFunction


class UnreferencedReusableObjectFunctionOptions(BaseModel):
    reusable_objects_location: str


class UnreferencedReusableObjectRuleThen(BaseModel):
    function: CoreFunction = CoreFunction.UNREFERENCED_REUSABLE_OBJECT
    function_options: UnreferencedReusableObjectFunctionOptions


@dataclass
class UnreferencedReusableObjectFunctionInputs:
    rule_name: str
    context: str
    target_value: Any
    options: UnreferencedReusableObjectFunctionOptions
    field = None
