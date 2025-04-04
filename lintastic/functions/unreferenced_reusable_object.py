from typing import Any, List

from lintastic.entities.functions.inputs import FunctionInputs


def _ref_exists(data: Any, reusable_objects_location: str) -> bool:
    if isinstance(data, dict):
        for key, value in data.items():
            if (
                key == '$ref'
                and isinstance(value, str)
                and value == reusable_objects_location
            ):
                return True
            if isinstance(value, dict) and _ref_exists(
                value, reusable_objects_location
            ):
                return True
            elif isinstance(value, list):
                for item in value:
                    if _ref_exists(item, reusable_objects_location):
                        return True
    if isinstance(data, list):
        for item in data:
            if _ref_exists(item, reusable_objects_location):
                return True
    if isinstance(data, str) and data == reusable_objects_location:
        return True
    return False


def unreferencedReusableObject(
    inputs: FunctionInputs
) -> List[str]:
    reusable_objects_location = inputs.options.reusable_objects_location
    if not _ref_exists(inputs.target_value, reusable_objects_location):
        return [
            f'No reference to {reusable_objects_location} was found '
            f'in {inputs.context}.'
        ]
    return []
