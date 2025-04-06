from typing import List

from lintastic.core.entities.functions.alphabetical import (
    AlphabeticalFunctionInputs,
)


def alphabetical(inputs: AlphabeticalFunctionInputs) -> List[str]:
    field_target_value = inputs.target_value.get(inputs.field)
    keyed_by = inputs.options.keyed_by
    if isinstance(field_target_value, list) and keyed_by:
        keys = [
            item.get(keyed_by)
            for item in field_target_value
            if keyed_by in item
        ]
        if keys != sorted(keys):
            return [
                (
                    f'{inputs.context} should have alphabetical '
                    f'"{inputs.field}" by {keyed_by}.'
                )
            ]
    return []
