from typing import Any, Dict, List, Union

from pydantic import BaseModel

from lintastic.enums.severity import Severity


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
