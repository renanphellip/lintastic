from pydantic import BaseModel

from lintastic.enums.core_function import CoreFunction


class DefinedRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.DEFINED
