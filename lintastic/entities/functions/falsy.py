from pydantic import BaseModel

from lintastic.enums import CoreFunction


class FalsyRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.FALSY
