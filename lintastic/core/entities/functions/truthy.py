from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel

from lintastic.core.enums.core_function import CoreFunction


class TruthyRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.TRUTHY


@dataclass
class TruthyFunctionInputs:
    rule_name: str
    context: str
    target_value: Any
    options = None
    field: str
