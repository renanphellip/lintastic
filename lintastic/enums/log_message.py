from enum import Enum


class LogMessage(str, Enum):
    INPUTS = 'Inputs: {inputs}'
    DISPLAY_VERSION = 'Lintastic CLI version: {lintastic_version}'
    VERSION_NOT_SPECIFIED = 'Lintastic version was not specified.'
    DOCUMENT_RESOLVED = 'Document resolved to: {resolved_document_path}'
    INVALID_FILE_EXTENSION = (
        'The file path "{file_path}" does not have a '
        'valid extension: {supported_extensions}'
    )
    VALID_FILE_EXTENSION = 'Valid extension: {file_path}'
    FILE_NOT_FOUND = 'The file path "{file_path}" was not found.'
    FILE_EXISTS = 'File exists: {file_path}'
    UNSUPPORTED_FILE_EXTENSION = 'Unsupported file extension: {file_path}'
    READING_FILE = 'Reading: {file_path}'
    CIRCULAR_REFERENCE = (
        'Failed to read: {file_path}\n'
        'There is possibly a circular reference in the document '
        'that references this file.'
    )
    FAIL_TO_READ_FILE = 'Failed to read: {file_path}\n{error}'
    RESOLVING_FILE = 'Resolving: {document_path}'
    FAIL_TO_RESOLVE_FILE = 'Failed to resolve: {document_path}\n{error}'
    CREATING_DIRECTORY = 'Creating directory: {output_dir}'
    FAIL_TO_CREATE = 'Failed to create: {output_path}\n{error}'
    CREATING_OUTPUT_FILE = 'Creating: {output_path}'
    INVALID_RULESET_SCHEMA = 'Invalid ruleset schema: {error}'
    EMPTY_FUNCTION = 'The function property must not be empty.'
    FAIL_TO_CREATE_RULE = 'Rule name: {rule_name}\nException: {error}'
    INIT_NOT_FOUND = (
        'The file "__init__.py" was not found in: {custom_functions_path}'
    )
    FUNCTION_ALREADY_EXISTS = (
        'The core function "{function_name}" already '
        'exists. The custom function with the same name will not be used.'
    )
    CUSTOM_FUNCTION_IMPORTED = 'Imported custom function: {function_name}'
    RULESET_FUNCTIONS_NOT_FOUND = (
        'The following ruleset functions was not found: {functions}'
    )
    JSONPATH_RESULTS_LENGTH = (
        '{results_len} occurrences were found for JSONPath pattern: '
        '{jsonpath_pattern}'
    )
    FAIL_TO_PARSE_JSONPATH = (
        'Failed to parse JSONPath "{jsonpath_pattern}": {error}'
    )
    FAIL_TO_VALIDATE_DOCUMENT = (
        'Failed to validate the document "{document_path}": {error}'
    )
    PROCESSING_RULE = 'Processing rule: {rule_name}'
    RUNNING_FUNCTION = (
        'Running "{function_name}" function for given: {jsonpath_match}'
    )
    FAIL_TO_WRITE_FILE_WITH_INVALID_TYPE = (
        'Failed to write "{output_path}". '
        'Data must be an instance of "DiagnosticCollection".'
    )
    RESULTS_EXPORTED = 'Results exported to: {results_path}'

    def __str__(self):
        return self.value
