from typing import Any, Dict, Optional, Protocol, Union

from lintastic.core.entities.functions.alphabetical import AlphabeticalFunctionOptions
from lintastic.core.entities.functions.casing import CasingFunctionOptions
from lintastic.core.entities.functions.enumeration import EnumerationFunctionOptions
from lintastic.core.entities.functions.length import LengthFunctionOptions
from lintastic.core.entities.functions.pattern import PatternFunctionOptions
from lintastic.core.entities.functions.schema import SchemaFunctionOptions
from lintastic.core.entities.functions.typed_enum import TypedEnumFunctionOptions
from lintastic.core.entities.functions.unreferenced_reusable_object import (
    UnreferencedReusableObjectFunctionOptions,
)
from lintastic.core.entities.functions.xor import XORFunctionOptions


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
