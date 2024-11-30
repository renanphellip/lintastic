from typing import Any, Dict, List


def truthy(
    context: str, target_value: Dict[str, Any], field: str, verbose: bool
) -> List[str]:
    falsy_values = (False, '', 0, None)
    if target_value.get(field) in falsy_values:
        return [f'{context}.{field} must not be: empty string, 0, false, null']
    return []
