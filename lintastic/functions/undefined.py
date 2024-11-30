from typing import Any, Dict, List


def undefined(
    context: str, target_value: Dict[str, Any], field: str, verbose: bool
) -> List[str]:
    if target_value.get(field) is not None:
        return [f'{context}.{field} must be null.']
    return []
