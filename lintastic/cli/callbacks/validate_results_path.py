import typer

from lintastic.core.enums.supported_result_extension import SupportedResultExtension
from lintastic.utils.file_validator import FileValidator


def validate_results_path(results_path: str) -> str:
    if results_path:
        valid_extension, error_message = FileValidator.validate_extension(results_path, SupportedResultExtension)
        if not valid_extension:
            raise typer.BadParameter(error_message)
    return results_path
