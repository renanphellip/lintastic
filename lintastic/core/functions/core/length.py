from typing import Any, List, Union

from lintastic.core.entities.functions.length import LengthFunctionInputs


def length(inputs: LengthFunctionInputs) -> List[str]:
    min_length = inputs.options.min
    max_length = inputs.options.max
    has_min_length = min_length != -1
    has_max_length = max_length != -1
    field_target_value = inputs.target_value.get(inputs.field)
    min_length_failed = not _check_min_length(field_target_value, min_length)
    max_length_failed = not _check_max_length(field_target_value, max_length)

    messages = []

    if has_min_length and min_length_failed:
        message = f'The {inputs.field} value in {inputs.context}'
        if isinstance(field_target_value, (str, list, dict)):
            message += f' must have a length greater than or equal to {min_length}.'
        else:
            message += f' must be a number greater than or equal to {min_length}.'
        messages.append(message)

    if has_max_length and max_length_failed:
        message = f'The {inputs.field} value in {inputs.context}'
        if isinstance(field_target_value, (str, list, dict)):
            message += f' must have a length less than or equal to {max_length}.'
        else:
            message += f' must be a number less than or equal to {max_length}.'
        messages.append(message)

    return messages


def _check_min_length(value: Any, min_length: Union[int, float]) -> bool:
    if min_length == -1:
        return True
    if isinstance(value, (str, list, dict)):
        return len(value) >= min_length
    if isinstance(value, (int, float)):
        return value >= min_length
    return False


def _check_max_length(value: Any, max_length: Union[int, float]) -> bool:
    if max_length == -1:
        return True
    if isinstance(value, (str, list, dict)):
        return len(value) <= max_length
    if isinstance(value, (int, float)):
        return value <= max_length
    return False
