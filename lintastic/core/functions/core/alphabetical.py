from typing import List

from lintastic.core.entities.functions.alphabetical import (
    AlphabeticalFunctionInputs,
)


def alphabetical(inputs: AlphabeticalFunctionInputs) -> List[str]:
    path = f'{inputs.context}.{inputs.field}'
    field_target_value = inputs.target_value.get(inputs.field)
    keyed_by = inputs.options.keyed_by

    if isinstance(field_target_value, dict):
        keys = list(field_target_value.keys())
        if keys != sorted(keys):
            return [f'"{path}" object should have alphabetical keys.']

    elif isinstance(field_target_value, list):
        if keyed_by:
            keyed_values = [item.get(keyed_by) for item in field_target_value if isinstance(item, dict) and keyed_by in item]
            if keyed_values != sorted(keyed_values):
                return [f'"{path}" list should have alphabetical objects sorted by "{keyed_by}".']
        elif field_target_value != sorted(field_target_value):
            return [f'"{path}" list should have alphabetical values.']

    return []
