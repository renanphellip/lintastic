from typing import List

from lintastic.entities.functions.inputs import FunctionInputs

def defined(
    inputs: FunctionInputs
) -> List[str]:
    if inputs.target_value.get(inputs.field) is None:
        return [f'{inputs.context}.{inputs.field} must not be null.']
    return []
