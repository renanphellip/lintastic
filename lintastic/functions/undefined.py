from typing import List

from lintastic.entities.functions.inputs import FunctionInputs


def undefined(
    inputs: FunctionInputs
) -> List[str]:
    if inputs.target_value.get(inputs.field) is not None:
        return [f'{inputs.context}.{inputs.field} must be null.']
    return []
