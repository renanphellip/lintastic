from dataclasses import dataclass
from typing import Any, Dict, Union
from . import (
    AlphabeticalFunctionOptions,
    CasingFunctionOptions,
    EnumerationFunctionOptions,
    LengthFunctionOptions,
    PatternFunctionOptions,
    SchemaFunctionOptions,
    TypedEnumFunctionOptions,
    UnreferencedReusableObjectFunctionOptions,
    XORFunctionOptions
)

@dataclass
class FunctionInputs:
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
        None
    ] = None
    field: Union[str, None] = None
    verbose: bool = False
