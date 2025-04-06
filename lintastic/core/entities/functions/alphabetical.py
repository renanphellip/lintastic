from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel

from lintastic.core.enums.core_function import CoreFunction


class AlphabeticalFunctionOptions(BaseModel):
    keyed_by: str


class AlphabeticalRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.ALPHABETICAL
    function_options: AlphabeticalFunctionOptions


@dataclass
class AlphabeticalFunctionInputs:
    rule_name: str
    context: str
    target_value: Any
    options: AlphabeticalFunctionOptions
    field: str
