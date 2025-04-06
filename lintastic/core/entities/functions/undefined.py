from dataclasses import dataclass
from typing import Any, Union

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
    field: Union[str, None] = None
    verbose: bool = False
