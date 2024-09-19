from typing import Any, Dict

from pydantic import BaseModel


class CustomRuleThen(BaseModel):
    field: str = ''
    function: str
    function_options: Dict[str, Any] = {}
