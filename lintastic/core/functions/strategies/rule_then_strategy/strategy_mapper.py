from lintastic.core.enums.core_function import CoreFunction
from lintastic.core.enums.log_message import LogMessage

from .alphabetical import AlphabeticalRuleThenStrategy
from .casing import CasingRuleThenStrategy
from .custom import CustomRuleThenStrategy
from .defined import DefinedRuleThenStrategy
from .enumeration import EnumerationRuleThenStrategy
from .falsy import FalsyRuleThenStrategy
from .length import LengthRuleThenStrategy
from .pattern import PatternRuleThenStrategy
from .schema import SchemaRuleThenStrategy
from .strategy import RuleThenStrategy
from .truthy import TruthyRuleThenStrategy
from .typed_enum import TypedEnumRuleThenStrategy
from .undefined import UndefinedRuleThenStrategy
from .unreferenced_reusable_object import (
    UnreferencedReusableObjectRuleThenStrategy,
)
from .xor import XORRuleThenStrategy


class RuleThenStrategyMapper:
    def __init__(self):
        self.function_strategy_mapping = {
            CoreFunction.ALPHABETICAL: AlphabeticalRuleThenStrategy(),
            CoreFunction.CASING: CasingRuleThenStrategy(),
            CoreFunction.DEFINED: DefinedRuleThenStrategy(),
            CoreFunction.ENUMERATION: EnumerationRuleThenStrategy(),
            CoreFunction.FALSY: FalsyRuleThenStrategy(),
            CoreFunction.LENGTH: LengthRuleThenStrategy(),
            CoreFunction.PATTERN: PatternRuleThenStrategy(),
            CoreFunction.SCHEMA: SchemaRuleThenStrategy(),
            CoreFunction.TRUTHY: TruthyRuleThenStrategy(),
            CoreFunction.TYPED_ENUM: TypedEnumRuleThenStrategy(),
            CoreFunction.UNDEFINED: UndefinedRuleThenStrategy(),
            # ruff: noqa: E501
            CoreFunction.UNREFERENCED_REUSABLE_OBJECT: UnreferencedReusableObjectRuleThenStrategy(),
            CoreFunction.XOR: XORRuleThenStrategy(),
        }

    def get_strategy(self, function_name: str) -> RuleThenStrategy:
        if not function_name:
            raise ValueError(LogMessage.EMPTY_FUNCTION)
        try:
            core_function = CoreFunction(function_name.lower())
        except:
            core_function = None
        return self.function_strategy_mapping.get(
            core_function, CustomRuleThenStrategy()
        )
