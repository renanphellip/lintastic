from enum import Enum


class CoreFunction(str, Enum):
    ALPHABETICAL = 'alphabetical'
    CASING = 'casing'
    DEFINED = 'defined'
    ENUMERATION = 'enumeration'
    FALSY = 'falsy'
    LENGTH = 'length'
    PATTERN = 'pattern'
    SCHEMA = 'schema'
    TRUTHY = 'truthy'
    TYPED_ENUM = 'typedEnum'
    UNDEFINED = 'undefined'
    UNREFERENCED_REUSABLE_OBJECT = 'unreferencedReusableObject'
    XOR = 'xor'

    def __str__(self):
        return self.value
