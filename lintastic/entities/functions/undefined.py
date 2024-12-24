from pydantic import BaseModel

from lintastic.enums import CoreFunction


class UndefinedRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.UNDEFINED
