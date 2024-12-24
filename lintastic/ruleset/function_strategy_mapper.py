from lintastic.enums import CoreFunction, LogMessage

from .function_strategies import (
    AlphabeticalFunctionStrategy,
    CasingFunctionStrategy,
    CustomFunctionStrategy,
    DefinedFunctionStrategy,
    EnumerationFunctionStrategy,
    FalsyFunctionStrategy,
    FunctionStrategy,
    LengthFunctionStrategy,
    PatternFunctionStrategy,
    SchemaFunctionStrategy,
    TruthyFunctionStrategy,
    TypedEnumFunctionStrategy,
    UndefinedFunctionStrategy,
    UnreferencedReusableObjectFunctionStrategy,
    XORFunctionStrategy,
)


class FunctionStrategyMapper:
    def __init__(self):
        self.function_strategy_mapping = {
            CoreFunction.ALPHABETICAL: AlphabeticalFunctionStrategy(),
            CoreFunction.CASING: CasingFunctionStrategy(),
            CoreFunction.DEFINED: DefinedFunctionStrategy(),
            CoreFunction.ENUMERATION: EnumerationFunctionStrategy(),
            CoreFunction.FALSY: FalsyFunctionStrategy(),
            CoreFunction.LENGTH: LengthFunctionStrategy(),
            CoreFunction.PATTERN: PatternFunctionStrategy(),
            CoreFunction.SCHEMA: SchemaFunctionStrategy(),
            CoreFunction.TRUTHY: TruthyFunctionStrategy(),
            CoreFunction.TYPED_ENUM: TypedEnumFunctionStrategy(),
            CoreFunction.UNDEFINED: UndefinedFunctionStrategy(),
            CoreFunction.UNREFERENCED_REUSABLE_OBJECT: UnreferencedReusableObjectFunctionStrategy(),
            CoreFunction.XOR: XORFunctionStrategy(),
        }

    def get_strategy(self, function_name: str) -> FunctionStrategy:
        if not function_name:
            raise ValueError(LogMessage.EMPTY_FUNCTION)
        try:
            core_function = CoreFunction(function_name.lower())
        except:
            core_function = None
        return self.function_strategy_mapping.get(
            core_function, CustomFunctionStrategy()
        )
