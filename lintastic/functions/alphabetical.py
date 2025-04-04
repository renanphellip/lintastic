from typing import List

from lintastic.entities.functions.inputs import FunctionInputs


def alphabetical(
    inputs: FunctionInputs
) -> List[str]:
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
                    f'"{inputs.context}" should have alphabetical "{inputs.field}" '
                    f'by {keyed_by}.'
                )
            ]
    return []
