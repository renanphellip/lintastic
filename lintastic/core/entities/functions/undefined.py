from dataclasses import dataclass
from typing import Any, Optional, Union

from pydantic import BaseModel

from lintastic.core.enums.core_function import CoreFunction


class UndefinedRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.UNDEFINED


@dataclass
class UndefinedFunctionInputs:
    rule_name: str
    context: str
    target_value: Any
    options = None
    field: Optional[str] = None
