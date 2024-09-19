from typing import List

from pydantic import BaseModel


class XORFunctionOptions(BaseModel):
    properties: List[str]


class XORRuleThen(BaseModel):
    function: str = 'xor'
    function_options: XORFunctionOptions
