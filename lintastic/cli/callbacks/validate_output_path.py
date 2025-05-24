import typer

from lintastic.core.enums.supported_document_extension import (
    SupportedDocumentExtension,
)
from lintastic.utils.file_validator import FileValidator


def validate_output_path(output_path: str) -> str:
    valid_extension, error_message = FileValidator.validate_extension(output_path, SupportedDocumentExtension)
    if not valid_extension:
        raise typer.BadParameter(error_message)
    return output_path
