from pydantic import BaseModel

from lintastic.enums.core_function import CoreFunction


class UndefinedRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.UNDEFINED
