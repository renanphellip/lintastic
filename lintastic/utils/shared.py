from typing import Any


def get_field_name_from_jsonpath_context(
    jsonpath_context: str, rule_then: Any
) -> str:
    return getattr(rule_then, 'field', jsonpath_context.split('.')[-1])
