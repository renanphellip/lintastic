from dataclasses import dataclass
from typing import Any, Dict, Optional, Union

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
    options: Optional[
        Dict[str, Any],
    ] = None
    field: Optional[str] = None
