import typer

from lintastic.core.enums.supported_document_extension import (
    SupportedDocumentExtension,
)
from lintastic.utils.file_validator import FileValidator


def validate_document_path(document_path: str) -> str:
    valid_extension, error_message = FileValidator.validate_extension(document_path, SupportedDocumentExtension)
    if not valid_extension:
        raise typer.BadParameter(error_message)
    file_exists, error_message = FileValidator.validate_existence(document_path)
    if not file_exists:
        raise typer.BadParameter(error_message)
    return document_path
