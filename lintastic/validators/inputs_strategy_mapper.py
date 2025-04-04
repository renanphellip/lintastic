from lintastic.enums.core_function import CoreFunction
from lintastic.enums.log_message import LogMessage

from .function_inputs_strategies import (
    AlphabeticalInputsStrategy,
    CasingInputsStrategy,
    CustomInputsStrategy,
    DefinedInputsStrategy,
    EnumerationInputsStrategy,
    FalsyInputsStrategy,
    FunctionInputsStrategy,
    LengthInputsStrategy,
    PatternInputsStrategy,
    SchemaInputsStrategy,
    TruthyInputsStrategy,
    TypedEnumInputsStrategy,
    UndefinedInputsStrategy,
    UnreferencedReusableObjectInputsStrategy,
    XORInputsStrategy,
)


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

    def get_strategy(self, function_name: str) -> FunctionInputsStrategy:
        if not function_name:
            raise ValueError(LogMessage.EMPTY_FUNCTION)
        try:
            core_function = CoreFunction(function_name.lower())
        except:
            core_function = None
        return self.inputs_strategy_mapping.get(
            core_function, CustomInputsStrategy()
        )
