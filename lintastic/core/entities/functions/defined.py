from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel

from lintastic.core.enums.core_function import CoreFunction


class DefinedRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.DEFINED


@dataclass
class DefinedFunctionInputs:
    rule_name: str
    context: str
    target_value: Any
    options = None
    field: str
    verbose: bool = False
