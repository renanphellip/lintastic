from typing import Any, Dict, List


def falsy(
    context: str,
    target_value: Dict[str, Any],
    field: str,
    verbose: bool,
    rule_name: str,
) -> List[str]:
    falsy_values = (False, '', 0, None)
    if target_value.get(field) not in falsy_values:
        return [f'{context}.{field} must be: empty string, 0, false, null']
    return []
