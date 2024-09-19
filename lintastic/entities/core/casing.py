from enum import Enum

from pydantic import BaseModel


class CasingType(str, Enum):
    FLAT = 'flat'
    CAMEL = 'camel'
    PASCAL = 'pascal'
    KEBAB = 'kebab'
    COBOL = 'cobol'
    SNAKE = 'snake'
    MACRO = 'macro'

    def __str__(self):
        return self.value


class CasingFunctionOptions(BaseModel):
    type: CasingType
    disallow_digits: bool = True
    separator_char: str = ''
    separator_allow_leading: bool = False


class CasingRuleThen(BaseModel):
    function: str = 'casing'
    function_options: CasingFunctionOptions
