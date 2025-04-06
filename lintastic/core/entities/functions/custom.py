from dataclasses import dataclass
from typing import Any, Dict, Union

from pydantic import BaseModel


class CustomRuleThen(BaseModel):
    field: str
    function: str
    function_options: Dict[str, Any]


@dataclass
class CustomFunctionInputs:
    rule_name: str
    context: str
    target_value: Any
    options: Union[
        Dict[str, Any],
        None,
    ] = None
    field: Union[str, None] = None
