from typing import List

from pydantic import BaseModel

from lintastic.enums.core_function import CoreFunction


class XORFunctionOptions(BaseModel):
    properties: List[str]


class XORRuleThen(BaseModel):
    function: CoreFunction = CoreFunction.XOR
    function_options: XORFunctionOptions
