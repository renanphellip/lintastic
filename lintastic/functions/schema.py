from typing import Any, Dict, List

from jsonschema import (
    Draft4Validator,
    Draft6Validator,
    Draft7Validator,
    Draft201909Validator,
    Draft202012Validator,
    validate,
)

from lintastic.entities.functions.schema import SchemaFunctionOptions


def schema(
    context: str,
    target_value: Dict[str, Any],
    function_options: SchemaFunctionOptions,
    field: str,
    verbose: bool,
    rule_name: str,
) -> List[str]:
    try:
        expected_schema = function_options.schema_definition
        dialect = function_options.dialect
        field_target_value = target_value.get(field)

        validator_classes = {
            'draft4': Draft4Validator,
            'draft6': Draft6Validator,
            'draft7': Draft7Validator,
            'draft2019-09': Draft201909Validator,
            'draft2020-12': Draft202012Validator,
        }

        if dialect == 'auto':
            validate(instance=field_target_value, schema=expected_schema)
        else:
            validator_class = validator_classes.get(dialect)
            if validator_class:
                validator = validator_class(expected_schema)
                errors = validator.iter_errors(field_target_value)
                exceptions = []
                for error in errors:
                    exceptions.append(error.message)
                if len(exceptions) > 0:
                    raise Exception(exceptions)
        return []
    except Exception as error:
        return_all_errors = function_options.all_errors
        if return_all_errors:
            return [
                f'{context}.{field} does not meet the expected schema: '
                + error
            ]
        return [
            f'{context}.{field} does not meet the expected schema: '
            + expected_schema
        ]
