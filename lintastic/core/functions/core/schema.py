from typing import List

from jsonschema import (
    Draft4Validator,
    Draft6Validator,
    Draft7Validator,
    Draft201909Validator,
    Draft202012Validator,
    validate,
)

from lintastic.core.entities.functions.schema import SchemaFunctionInputs


def schema(inputs: SchemaFunctionInputs) -> List[str]:
    try:
        expected_schema = inputs.options.schema_definition
        dialect = inputs.options.dialect
        field_target_value = inputs.target_value.get(inputs.field)

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
        return_all_errors = inputs.options.all_errors
        if return_all_errors:
            return [
                f'{inputs.context}.{inputs.field} does not meet the expected '
                f'schema: {error}'
            ]
        return [
            f'{inputs.context}.{inputs.field} does not meet the expected '
            f'schema: {expected_schema}'
        ]
