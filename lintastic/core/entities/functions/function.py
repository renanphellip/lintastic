from dataclasses import dataclass
from typing import Any, Dict, Protocol, Union

from .alphabetical import AlphabeticalFunctionOptions
from .casing import CasingFunctionOptions
from .enumeration import EnumerationFunctionOptions
from .length import LengthFunctionOptions
from .pattern import PatternFunctionOptions
from .schema import SchemaFunctionOptions
from .typed_enum import TypedEnumFunctionOptions
from .unreferenced_reusable_object import (
    UnreferencedReusableObjectFunctionOptions,
)
from .xor import XORFunctionOptions


@dataclass
class FunctionInputs(Protocol):
    rule_name: str
    context: str
    target_value: Any
    options: Union[
        AlphabeticalFunctionOptions,
        CasingFunctionOptions,
        EnumerationFunctionOptions,
        LengthFunctionOptions,
        PatternFunctionOptions,
        SchemaFunctionOptions,
        TypedEnumFunctionOptions,
        UnreferencedReusableObjectFunctionOptions,
        XORFunctionOptions,
        Dict[str, Any],
        None,
    ] = None
    field: Union[str, None] = None
