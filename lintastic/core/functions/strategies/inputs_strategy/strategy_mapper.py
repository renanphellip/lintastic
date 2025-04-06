from lintastic.core.enums.core_function import CoreFunction
from lintastic.core.enums.log_message import LogMessage

from .alphabetical import AlphabeticalInputsStrategy
from .casing import CasingInputsStrategy
from .custom import CustomInputsStrategy
from .defined import DefinedInputsStrategy
from .enumeration import EnumerationInputsStrategy
from .falsy import FalsyInputsStrategy
from .length import LengthInputsStrategy
from .pattern import PatternInputsStrategy
from .schema import SchemaInputsStrategy
from .strategy import InputsStrategy
from .truthy import TruthyInputsStrategy
from .typed_enum import TypedEnumInputsStrategy
from .undefined import UndefinedInputsStrategy
from .unreferenced_reusable_object import (
    UnreferencedReusableObjectInputsStrategy,
)
from .xor import XORInputsStrategy


class InputsStrategyMapper:
    def __init__(self):
        self.inputs_strategy_mapping = {
            CoreFunction.ALPHABETICAL: AlphabeticalInputsStrategy(),
            CoreFunction.CASING: CasingInputsStrategy(),
            CoreFunction.DEFINED: DefinedInputsStrategy(),
            CoreFunction.ENUMERATION: EnumerationInputsStrategy(),
            CoreFunction.FALSY: FalsyInputsStrategy(),
            CoreFunction.LENGTH: LengthInputsStrategy(),
            CoreFunction.PATTERN: PatternInputsStrategy(),
            CoreFunction.SCHEMA: SchemaInputsStrategy(),
            CoreFunction.TRUTHY: TruthyInputsStrategy(),
            CoreFunction.TYPED_ENUM: TypedEnumInputsStrategy(),
            CoreFunction.UNDEFINED: UndefinedInputsStrategy(),
            # ruff: noqa: E501
            CoreFunction.UNREFERENCED_REUSABLE_OBJECT: UnreferencedReusableObjectInputsStrategy(),
            CoreFunction.XOR: XORInputsStrategy(),
        }

    def get_strategy(self, function_name: str) -> InputsStrategy:
        if not function_name:
            raise ValueError(LogMessage.EMPTY_FUNCTION)
        try:
            core_function = CoreFunction(function_name.lower())
        except:
            core_function = None
        return self.inputs_strategy_mapping.get(
            core_function, CustomInputsStrategy()
        )
