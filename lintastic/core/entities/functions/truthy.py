from dataclasses import dataclass
from typing import Any, Union

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
    field: Union[str, None] = None
