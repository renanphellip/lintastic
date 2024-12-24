from pydantic import BaseModel

from lintastic.enums import CoreFunction
from lintastic.enums.casing import CasingType


class CasingFunctionOptions(BaseModel):
    type: CasingType
    disallow_digits: bool = True
    separator_char: str = ''
    separator_allow_leading: bool = False


class CasingRuleThen(BaseModel):
    function: CoreFunction = CoreFunction.CASING
    function_options: CasingFunctionOptions
