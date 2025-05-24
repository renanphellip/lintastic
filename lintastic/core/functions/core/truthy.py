from typing import List

from lintastic.core.entities.functions.truthy import TruthyFunctionInputs


def truthy(inputs: TruthyFunctionInputs) -> List[str]:
    falsy_values = (False, '', 0, None)
    if inputs.target_value.get(inputs.field) in falsy_values:
        return [f'{inputs.context}.{inputs.field} must not be: ' 'empty string, 0, false, null']
    return []
