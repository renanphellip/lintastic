from typing import Any, Dict, List


def defined(
    context: str,
    target_value: Dict[str, Any],
    field: str,
    verbose: bool,
    rule_name: str,
) -> List[str]:
    if target_value.get(field) is None:
        return [f'{context}.{field} must not be null.']
    return []
