from lintastic.logs import LogMessages

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
            'alphabetical': AlphabeticalFunctionStrategy(),
            'casing': CasingFunctionStrategy(),
            'defined': DefinedFunctionStrategy(),
            'enumeration': EnumerationFunctionStrategy(),
            'falsy': FalsyFunctionStrategy(),
            'length': LengthFunctionStrategy(),
            'pattern': PatternFunctionStrategy(),
            'schema': SchemaFunctionStrategy(),
            'truthy': TruthyFunctionStrategy(),
            'typedEnum': TypedEnumFunctionStrategy(),
            'undefined': UndefinedFunctionStrategy(),
            'unreferencedReusableObject':
                UnreferencedReusableObjectFunctionStrategy(),
            'xor': XORFunctionStrategy(),
        }

    def get_strategy(self, function_name: str) -> FunctionStrategy:
        if not function_name:
            raise ValueError(LogMessages.EMPTY_FUNCTION)
        return self.function_strategy_mapping.get(
            function_name.lower(), CustomFunctionStrategy()
        )
