from typing import List

from lintastic.entities.functions.inputs import FunctionInputs


def xor(inputs: FunctionInputs) -> List[str]:
    properties = inputs.options.properties
    properties_found = sum(
        1 for property in properties if property in inputs.target_value
    )
    if properties_found != 1:
        return [
            (
                f'{inputs.context} must have only one of these properties '
                f'defined: {properties}'
            )
        ]
    return []
