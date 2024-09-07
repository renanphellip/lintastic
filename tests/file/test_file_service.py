import pytest
from rich.console import Console
from lintastic.file.file_reader_factory import FileReaderFactory
from lintastic.file.file_service import FileService


@pytest.fixture
def mock_console(mocker):
    return mocker.MagicMock(spec=Console)

@pytest.fixture
def file_service(mock_console):
    return FileService(mock_console)

def test_read_file_success(mocker, file_service, mock_console):
    file_path = 'document.json'
    expected_result = {"key": "value"}

    mock_file_reader = mocker.MagicMock()
    mock_file_reader.read.return_value = expected_result
    mocker.patch.object(FileReaderFactory, 'get_file_reader', return_value=mock_file_reader)
    
    result = file_service.read_file(file_path)
    
    assert result == expected_result
    mock_console.print.assert_not_called()

def test_read_file_error(mocker, file_service, mock_console):
    file_path = 'document.json'
    absolute_file_path = f'/absolute/path/to/{file_path}'
    exception_message = "File not found"
    exception = Exception(exception_message)
    expected_error_message = f'[red]Failed to read the file "{absolute_file_path}": {exception_message}[/red]'

    mocker.patch.object(FileReaderFactory, 'get_file_reader', side_effect=exception)
    mocker.patch('os.path.abspath', return_value=absolute_file_path)
    
    with pytest.raises(SystemExit):
        file_service.read_file(file_path)
    
    mock_console.print.assert_called_once_with(expected_error_message)

def test_read_file_verbose(mocker, file_service, mock_console):
    file_path = 'document.json'
    absolute_file_path = f'/absolute/path/to/{file_path}'
    first_message = f'The absolute file path is: [blue]{absolute_file_path}[/blue]'
    second_message = f'Loading "[blue]{absolute_file_path}[/blue]"...'
    expected_result = {"key": "value"}

    mock_file_reader = mocker.MagicMock()
    mock_file_reader.read.return_value = expected_result
    mocker.patch.object(FileReaderFactory, 'get_file_reader', return_value=mock_file_reader)
    mocker.patch('os.path.abspath', return_value=absolute_file_path)
    
    result = file_service.read_file(file_path, verbose=True)
    
    assert result == expected_result
    mock_console.print.assert_any_call(first_message)
    mock_console.print.assert_any_call(second_message)
