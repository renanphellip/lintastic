from pydantic import BaseModel

from lintastic.enums.core_function import CoreFunction


class FalsyRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.FALSY
