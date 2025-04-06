from typing import List

from lintastic.entities.functions.inputs import FunctionInputs


def truthy(inputs: FunctionInputs) -> List[str]:
    falsy_values = (False, '', 0, None)
    if inputs.target_value.get(inputs.field) in falsy_values:
        return [
            f'{inputs.context}.{inputs.field} must not be: '
            'empty string, 0, false, null'
        ]
    return []
