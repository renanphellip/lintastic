from typing import Any, List


def get_field_name_from_jsonpath_context(
    jsonpath_context: str, rule_then: Any
) -> str:
    return getattr(rule_then, 'field', jsonpath_context.split('.')[-1])


def quote_unquoted_jsonpaths(jsonpath: str) -> str:
    paths = jsonpath.split('.')
    processed_paths = []
    for path in paths:
        if (
            '/' in path
            and not path.startswith(('"', "'"))
            and not path.endswith(('"', "'"))
        ):
            processed_paths.append(f'"{path}"')
        else:
            processed_paths.append(path)
    return '.'.join(processed_paths)


def transform_data_to_list(data: str) -> List[str]:
    return data if isinstance(data, list) else [data] if data else []
