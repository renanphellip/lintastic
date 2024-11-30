from typing import Any, Dict, List

from lintastic.entities.core.xor import XORFunctionOptions


def xor(
    context: str,
    target_value: Dict[str, Any],
    function_options: XORFunctionOptions,
    verbose: bool,
) -> List[str]:
    properties = function_options.properties
    properties_found = sum(
        1 for property in properties if property in target_value
    )
    if properties_found != 1:
        return [
            f'{context} must have only one of these properties defined: '
            + properties
        ]
    return []
