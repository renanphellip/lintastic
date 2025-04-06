from typing import List

from lintastic.entities.functions.inputs import FunctionInputs


def enumeration(inputs: FunctionInputs) -> List[str]:
    possible_values = inputs.options.values
    field_target_value = inputs.target_value.get(inputs.field)
    if isinstance(possible_values, list):
        if field_target_value not in possible_values:
            return [
                f'{inputs.context}.{inputs.field} must be: {possible_values}'
            ]
    return []
