from pydantic import BaseModel

from lintastic.enums.core_function import CoreFunction


class TruthyRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.TRUTHY
