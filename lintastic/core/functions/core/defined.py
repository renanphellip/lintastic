from typing import List

from lintastic.core.entities.functions.defined import DefinedFunctionInputs


def defined(inputs: DefinedFunctionInputs) -> List[str]:
    if inputs.target_value.get(inputs.field) is None:
        return [f'{inputs.context}.{inputs.field} must not be null.']
    return []
