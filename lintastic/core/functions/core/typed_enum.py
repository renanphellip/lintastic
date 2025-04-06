from typing import List

from lintastic.core.entities.functions.typed_enum import (
    TypedEnumFunctionInputs,
)


def typedEnum(inputs: TypedEnumFunctionInputs) -> List[str]:
    opt_enum = inputs.options.enum
    opt_type = inputs.options.type
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
            if not isinstance(inputs.target_value, data_types.get(opt_type)):
                messages.append(
                    f'The value {inputs.target_value} in {inputs.context} '
                    f'must be of type {opt_type}.'
                )
        if inputs.target_value not in opt_enum:
            messages.append(f'{inputs.context} must be: {opt_enum}')
    return messages
