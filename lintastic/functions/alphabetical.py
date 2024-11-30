from typing import Any, Dict, List

from lintastic.entities.core.alphabetical import AlphabeticalFunctionOptions


def alphabetical(
    context: str,
    target_value: Dict[str, Any],
    function_options: AlphabeticalFunctionOptions,
    field: str,
    verbose: bool,
) -> List[str]:
    field_target_value = target_value.get(field)
    keyed_by = function_options.keyed_by
    if isinstance(field_target_value, list) and keyed_by:
        keys = [
            item.get(keyed_by)
            for item in field_target_value
            if keyed_by in item
        ]
        if keys != sorted(keys):
            return [
                f'{context} should have alphabetical {field} by {keyed_by}.'
            ]
    return []
