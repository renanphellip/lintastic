from pydantic import BaseModel

from lintastic.enums import CoreFunction


class DefinedRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.DEFINED
