from typing import Any, Dict, List

from lintastic.entities.functions.enumeration import (
    EnumerationFunctionOptions,
)


def enumeration(
    context: str,
    target_value: Dict[str, Any],
    function_options: EnumerationFunctionOptions,
    field: str,
    verbose: bool,
    rule_name: str,
) -> List[str]:
    possible_values = function_options.values
    field_target_value = target_value.get(field)
    if isinstance(possible_values, list):
        if field_target_value not in possible_values:
            return [f'{context}.{field} must be: {possible_values}']
    return []
