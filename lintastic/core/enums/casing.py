from enum import Enum


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
