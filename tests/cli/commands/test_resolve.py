import pytest
from typer.testing import CliRunner
from lintastic.cli.commands.resolve import resolve
from lintastic.core.enums.log_message import LogMessage
from lintastic.core.enums.supported_document_extension import SupportedDocumentExtension
from lintastic.core.services.document_resolver_service import DocumentResolveService
from lintastic.io.writers.file_writer_service import FileWriterService
from lintastic.utils.file_validator import FileValidator
from lintastic.utils.logger import Logger

runner = CliRunner()

@pytest.fixture
def mock_logger_info(mocker):
    return mocker.patch.object(Logger, 'info')

@pytest.fixture
def mock_logger_success(mocker):
    return mocker.patch.object(Logger, 'success')

@pytest.fixture
def mock_validate_extension(mocker):
    return mocker.patch.object(FileValidator, 'validate_extension')

@pytest.fixture
def mock_validate_existence(mocker):
    return mocker.patch.object(FileValidator, 'validate_existence')

@pytest.fixture
def mock_resolve(mocker):
    return mocker.patch.object(DocumentResolveService, 'resolve')

@pytest.fixture
def mock_write_file(mocker):
    return mocker.patch.object(FileWriterService, 'write_file')

def test_resolve_success(
    mock_logger_info,
    mock_logger_success,
    mock_validate_extension,
    mock_validate_existence,
    mock_resolve,
    mock_write_file,
):
    # Arrange
    mock_resolve.return_value = {"key": "value"}
    mock_write_file.return_value = "/absolute/path/to/output.yml"

    # Act
    result = runner.invoke(
        resolve,
        [
            "input.yml",
            "output.yml",
            "--verbose",
        ],
    )

    # Assertions
    assert result.exit_code == 0
    mock_logger_info.assert_called()
    mock_logger_success.assert_called_with(
        LogMessage.DOCUMENT_RESOLVED.format(
            resolved_document_path="/absolute/path/to/output.yml"
        )
    )
    mock_validate_extension.assert_any_call("input.yml", SupportedDocumentExtension)
    mock_validate_extension.assert_any_call("output.yml", SupportedDocumentExtension)
    mock_validate_existence.assert_called_once_with("input.yml")
    mock_resolve.assert_called_once_with("input.yml")
    mock_write_file.assert_called_once_with("output.yml", {"key": "value"})

def test_resolve_invalid_extension(
    mock_logger_info,
    mock_validate_extension,
):
    # Arrange
    mock_validate_extension.side_effect = ValueError("Invalid file extension")

    # Act
    result = runner.invoke(
        resolve,
        [
            "input.txt",
            "output.yml",
            "--verbose",
        ],
    )

    # Assertions
    assert result.exit_code != 0
    mock_logger_info.assert_called()
    mock_validate_extension.assert_any_call("input.txt", SupportedDocumentExtension)

def test_resolve_file_not_found(
    mock_logger_info,
    mock_validate_existence,
):
    # Arrange
    mock_validate_existence.side_effect = FileNotFoundError("File not found")

    # Act
    result = runner.invoke(
        resolve,
        [
            "nonexistent.yml",
            "output.yml",
            "--verbose",
        ],
    )

    # Assertions
    assert result.exit_code != 0
    mock_logger_info.assert_called()
    mock_validate_existence.assert_called_once_with("nonexistent.yml")