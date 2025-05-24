from lintastic.core.enums.core_function import CoreFunction
from lintastic.core.interfaces.rule_then_strategy import IRuleThenStrategy

from .rule_then_strategy.alphabetical import AlphabeticalRuleThenStrategy
from .rule_then_strategy.casing import CasingRuleThenStrategy
from .rule_then_strategy.custom import CustomRuleThenStrategy
from .rule_then_strategy.defined import DefinedRuleThenStrategy
from .rule_then_strategy.enumeration import EnumerationRuleThenStrategy
from .rule_then_strategy.falsy import FalsyRuleThenStrategy
from .rule_then_strategy.length import LengthRuleThenStrategy
from .rule_then_strategy.pattern import PatternRuleThenStrategy
from .rule_then_strategy.schema import SchemaRuleThenStrategy
from .rule_then_strategy.truthy import TruthyRuleThenStrategy
from .rule_then_strategy.typed_enum import TypedEnumRuleThenStrategy
from .rule_then_strategy.undefined import UndefinedRuleThenStrategy
from .rule_then_strategy.unreferenced_reusable_object import (
    UnreferencedReusableObjectRuleThenStrategy,
)
from .rule_then_strategy.xor import XORRuleThenStrategy


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

    def get_strategy(self, function_name: str) -> IRuleThenStrategy:
        core_function = CoreFunction(str(function_name).lower())
        return self.function_strategy_mapping.get(core_function, CustomRuleThenStrategy())
