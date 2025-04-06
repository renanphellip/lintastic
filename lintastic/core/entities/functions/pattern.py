from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel

from lintastic.core.enums.core_function import CoreFunction


class PatternFunctionOptions(BaseModel):
    match: str = ''
    not_match: str = ''


class PatternRuleThen(BaseModel):
    function: CoreFunction = CoreFunction.PATTERN
    function_options: PatternFunctionOptions


@dataclass
class PatternFunctionInputs:
    rule_name: str
    context: str
    target_value: Any
    options: PatternFunctionOptions
    field = None
