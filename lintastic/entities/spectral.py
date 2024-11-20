from enum import Enum
from typing import Any, Dict, List, Union

from pydantic import BaseModel


class Severity(str, Enum):
    ERROR = 'error'
    WARN = 'warn'
    INFO = 'information'
    HINT = 'hint'

    def __str__(self):
        return self.value


class SpectralRuleThen(BaseModel):
    field: str = ''
    function: str
    functionOptions: Dict[str, Any] = {}


class SpectralRule(BaseModel):
    description: str = ''
    message: Union[str, List[str]] = ''
    documentation: Union[str, List[str]] = ''
    severity: Severity = Severity.WARN
    resolved: bool = True
    given: Union[str, List[str]]
    then: Union[SpectralRuleThen, List[SpectralRuleThen]]


class SpectralRuleset(BaseModel):
    rules: Dict[str, SpectralRule]
