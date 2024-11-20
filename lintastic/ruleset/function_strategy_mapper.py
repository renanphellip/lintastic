from .function_strategies import *

class FunctionStrategyMapper:
    def __init__(self):
        self.function_strategy_mapping = {
            'alphabetical': AlphabeticalFunctionStrategy,
            'casing': CasingFunctionStrategy,
            'defined': DefinedFunctionStrategy,
            'enumeration': EnumerationFunctionStrategy,
            'falsy': FalsyFunctionStrategy,
            'length': LengthFunctionStrategy,
            'pattern': PatternFunctionStrategy,
            'schema': SchemaFunctionStrategy,
            'truthy': TruthyFunctionStrategy,
            'typedEnum': TypedEnumFunctionStrategy,
            'undefined': UndefinedFunctionStrategy,
            'unreferencedReusableObject': UnreferencedReusableObjectFunctionStrategy,
            'xor': XORFunctionStrategy,
        }

    def get_strategy(self, function_name: str) -> FunctionStrategy:
        if not function_name:
            raise ValueError(
                'The function property must not be empty.'
            )
        return self.function_strategy_mapping.get(function_name.lower(), CustomFunctionStrategy)
