from typing import List

from lintastic.core.entities.functions.undefined import UndefinedFunctionInputs


def undefined(inputs: UndefinedFunctionInputs) -> List[str]:
    if inputs.target_value.get(inputs.field) is not None:
        return [f'{inputs.context}.{inputs.field} must be null.']
    return []
