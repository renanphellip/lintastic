from typing import List

from lintastic.core.entities.functions.falsy import FalsyFunctionInputs


def falsy(inputs: FalsyFunctionInputs) -> List[str]:
    falsy_values = (False, '', 0, None)
    if inputs.target_value.get(inputs.field) not in falsy_values:
        return [f'{inputs.context}.{inputs.field} must be: ' 'empty string, 0, false, null']
    return []
