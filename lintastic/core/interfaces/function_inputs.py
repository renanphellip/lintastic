from dataclasses import dataclass
from typing import Any, Dict, Optional, Protocol, Union

from ..entities.functions.alphabetical import AlphabeticalFunctionOptions
from ..entities.functions.casing import CasingFunctionOptions
from ..entities.functions.enumeration import EnumerationFunctionOptions
from ..entities.functions.length import LengthFunctionOptions
from ..entities.functions.pattern import PatternFunctionOptions
from ..entities.functions.schema import SchemaFunctionOptions
from ..entities.functions.typed_enum import TypedEnumFunctionOptions
from ..entities.functions.unreferenced_reusable_object import (
    UnreferencedReusableObjectFunctionOptions,
)
from ..entities.functions.xor import XORFunctionOptions
from abc import ABC

class IFunctionInputs(Protocol):
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
    field: Optional[str]
