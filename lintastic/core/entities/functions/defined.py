from dataclasses import dataclass
from typing import Any, Optional

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
    field: Optional[str] = None
