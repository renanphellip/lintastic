from typing import Any, Dict, List, Union

from lintastic.entities.core.length import LengthFunctionOptions


def _check_max_length(value: Any, max_length: Union[int, float]) -> bool:
    if max_length == -1:
        return True
    if isinstance(value, (str, list, dict)):
        return len(value) <= max_length
    if isinstance(value, (int, float)):
        return value <= max_length
    return False


def _check_min_length(value: Any, min_length: Union[int, float]) -> bool:
    if min_length == -1:
        return True
    if isinstance(value, (str, list, dict)):
        return len(value) >= min_length
    if isinstance(value, (int, float)):
        return value >= min_length
    return False


def length(
    context: str,
    target_value: Dict[str, Any],
    function_options: LengthFunctionOptions,
    field: str,
    verbose: bool,
) -> List[str]:
    min_length = function_options.min
    max_length = function_options.max
    has_min_length = min_length != -1
    has_max_length = max_length != -1
    field_target_value = target_value.get(field)
    min_length_failed = not _check_min_length(field_target_value, min_length)
    max_length_failed = not _check_max_length(field_target_value, max_length)

    messages = []

    if has_min_length and min_length_failed:
        message = f'The {field} value in {context}'
        if isinstance(field_target_value, (str, list, dict)):
            message += (
                f' must have a length greater than or equal to {min_length}.'
            )
        else:
            message += (
                f' must be a number greater than or equal to {min_length}.'
            )
        messages.append(message)

    if has_max_length and max_length_failed:
        message = f'The {field} value in {context}'
        if isinstance(field_target_value, (str, list, dict)):
            message += (
                f' must have a length less than or equal to {max_length}.'
            )
        else:
            message += f' must be a number less than or equal to {max_length}.'
        messages.append(message)

    return messages
