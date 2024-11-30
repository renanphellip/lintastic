from typing import List, Union

from lintastic.entities.core.typed_enum import TypedEnumFunctionOptions


def typedEnum(
    context: str,
    target_value: Union[str, int, float, bool],
    function_options: TypedEnumFunctionOptions,
    verbose: bool,
) -> List[str]:
    opt_enum = function_options.enum
    opt_type = function_options.type
    data_types = {
        'string': str,
        'integer': int,
        'number': (int, float),
        'boolean': bool,
    }
    messages = []
    if isinstance(opt_enum, list):
        if opt_type in data_types:
            for item in opt_enum:
                if not isinstance(item, data_types.get(opt_type)):
                    messages.append(
                        f'The enum value {item} must be of type {opt_type}.'
                    )
            if not isinstance(target_value, data_types.get(opt_type)):
                messages.append(
                    f'The value {target_value} in {context} must be '
                    f'of type {opt_type}.'
                )
        if target_value not in opt_enum:
            messages.append(f'{context} must be: {opt_enum}')
    return messages
