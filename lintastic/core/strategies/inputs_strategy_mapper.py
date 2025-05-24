from lintastic.core.enums.core_function import CoreFunction
from lintastic.core.enums.log_message import LogMessage

from .inputs_strategy.alphabetical import AlphabeticalInputsStrategy
from .inputs_strategy.casing import CasingInputsStrategy
from .inputs_strategy.custom import CustomInputsStrategy
from .inputs_strategy.defined import DefinedInputsStrategy
from .inputs_strategy.enumeration import EnumerationInputsStrategy
from .inputs_strategy.falsy import FalsyInputsStrategy
from .inputs_strategy.length import LengthInputsStrategy
from .inputs_strategy.pattern import PatternInputsStrategy
from .inputs_strategy.schema import SchemaInputsStrategy
from lintastic.core.interfaces.inputs_strategy import IInputsStrategy
from .inputs_strategy.truthy import TruthyInputsStrategy
from .inputs_strategy.typed_enum import TypedEnumInputsStrategy
from .inputs_strategy.undefined import UndefinedInputsStrategy
from .inputs_strategy.unreferenced_reusable_object import (
    UnreferencedReusableObjectInputsStrategy,
)
from .inputs_strategy.xor import XORInputsStrategy


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

    def get_strategy(self, function_name: str) -> IInputsStrategy:
        core_function = CoreFunction(str(function_name).lower())
        return self.inputs_strategy_mapping.get(core_function, CustomInputsStrategy())
