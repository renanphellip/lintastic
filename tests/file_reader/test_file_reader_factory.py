import pytest
from lintastic.file_reader.file_reader_factory import FileReaderFactory
from lintastic.file_reader.json_file_reader import JsonFileReader
from lintastic.file_reader.toml_file_reader import TomlFileReader
from lintastic.file_reader.yaml_file_reader import YamlFileReader


def test_get_file_reader_toml():
    file_path = 'pyproject.toml'
    file_reader = FileReaderFactory.get_file_reader(file_path)
    assert isinstance(file_reader, TomlFileReader)

def test_get_file_reader_json():
    file_path = 'document.json'
    file_reader = FileReaderFactory.get_file_reader(file_path)
    assert isinstance(file_reader, JsonFileReader)

@pytest.mark.parametrize("file_path", ["document.yaml", "document.yml"])
def test_get_file_reader_yaml(file_path):
    file_reader = FileReaderFactory.get_file_reader(file_path)
    assert isinstance(file_reader, YamlFileReader)

def test_get_file_reader_unsupported_extension(mocker):
    file_path = 'document.txt'
    expected_error_message = '[red]Unsupported file extension: document.txt[/red]'
    mock_exit = mocker.patch('sys.exit')
    mock_print = mocker.patch('rich.console.Console.print')
    FileReaderFactory.get_file_reader(file_path)
    mock_print.assert_called_once_with(expected_error_message)
    mock_exit.assert_called_once_with(1)

def test_get_file_reader_empty_string(mocker):
    file_path = ''
    expected_error_message = '[red]Unsupported file extension: [/red]'
    mock_exit = mocker.patch('sys.exit')
    mock_print = mocker.patch('rich.console.Console.print')
    FileReaderFactory.get_file_reader(file_path)
    mock_print.assert_called_once_with(expected_error_message)
    mock_exit.assert_called_once_with(1)

def test_get_file_reader_no_extension(mocker):
    file_path = 'document'
    expected_error_message = '[red]Unsupported file extension: document[/red]'
    mock_exit = mocker.patch('sys.exit')
    mock_print = mocker.patch('rich.console.Console.print')
    FileReaderFactory.get_file_reader(file_path)
    mock_print.assert_called_once_with(expected_error_message)
    mock_exit.assert_called_once_with(1)

def test_get_file_reader_uppercase_extension():
    file_path = 'pyproject.TOML'
    file_reader = FileReaderFactory.get_file_reader(file_path)
    assert isinstance(file_reader, TomlFileReader)
