import pytest
import tomli
from lintastic.file_reader.toml_file_reader import TomlFileReader


@pytest.fixture
def toml_reader():
    return TomlFileReader()

def test_read_toml(mocker, toml_reader):
    toml_content = b'key = "value"'
    expected_result = {"key": "value"}
    file_path = "dummy_path"

    mocker.patch("builtins.open", mocker.mock_open(read_data=toml_content))
    
    result = toml_reader.read(file_path)
    assert result == expected_result

def test_read_file_not_found(mocker, toml_reader):
    file_path = "non_existent_path"

    mocker.patch("builtins.open", side_effect=FileNotFoundError)
    
    with pytest.raises(FileNotFoundError):
        toml_reader.read(file_path)

def test_read_permission_error(mocker, toml_reader):
    file_path = "restricted_path"

    mocker.patch("builtins.open", side_effect=PermissionError)
    
    with pytest.raises(PermissionError):
        toml_reader.read(file_path)
