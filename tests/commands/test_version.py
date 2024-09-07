import pytest
from rich.console import Console
from lintastic.commands.version import version
from lintastic.file.file_service import FileService


def test_version_success(mocker):
    expected_version = '1.0.0'
    expected_message = f'\nLintastic CLI version: {expected_version}\n'
    toml_content = {
        'tool': {
            'poetry': {
                'version': f'{expected_version}'
            }
        }
    }

    mock_file_service = mocker.Mock(spec=FileService)
    mock_file_service.read_file.return_value = toml_content
    mock_print = mocker.patch('lintastic.commands.version.print')
    
    mocker.patch('lintastic.commands.version.FileService', return_value=mock_file_service)
    assert version() == True
    mock_print.assert_called_with(expected_message)

def test_version_key_error(mocker):
    expected_error_message = '\n[red]Lintastic version was not specified.[/red]\n'
    expected_exit_code = 1
    toml_content = {
        'tool': {
            'poetry': {}
        }
    }

    mock_file_service = mocker.Mock(spec=FileService)
    mock_file_service.read_file.return_value = toml_content
    
    mocker.patch('lintastic.commands.version.FileService', return_value=mock_file_service)
    mock_print = mocker.patch('lintastic.commands.version.print')
    with pytest.raises(SystemExit) as error:
        version()
    assert error.type == SystemExit
    assert error.value.code == expected_exit_code
    mock_print.assert_called_with(expected_error_message)

def test_version_invalid_format(mocker):
    expected_error_message = '\n[red]Lintastic version was not specified.[/red]\n'
    expected_exit_code = 1
    toml_content = {
        'tool': {
            'poetry': {
                'version': None
            }
        }
    }

    mock_file_service = mocker.Mock(spec=FileService)
    mock_file_service.read_file.return_value = toml_content
    mock_print = mocker.patch('lintastic.commands.version.print')
    
    mocker.patch('lintastic.commands.version.FileService', return_value=mock_file_service)
    with pytest.raises(SystemExit) as error:
        version()
    assert error.type == SystemExit
    assert error.value.code == expected_exit_code
    mock_print.assert_called_with(expected_error_message)