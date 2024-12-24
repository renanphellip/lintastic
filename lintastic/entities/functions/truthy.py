from pydantic import BaseModel

from lintastic.enums import CoreFunction


class TruthyRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.TRUTHY
