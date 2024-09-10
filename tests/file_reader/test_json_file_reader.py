import json
import pytest
from lintastic.file_reader.json_file_reader import JsonFileReader


@pytest.fixture
def json_reader():
    return JsonFileReader()

def test_read_json(mocker, json_reader):
    json_content = '{"key": "value"}'
    expected_result = {"key": "value"}
    file_path = "dummy_path"
    
    mocker.patch("builtins.open", mocker.mock_open(read_data=json_content))
    
    result = json_reader.read(file_path)
    assert result == expected_result

def test_read_file_not_found(mocker, json_reader):
    file_path = "non_existent_path"

    mocker.patch("builtins.open", side_effect=FileNotFoundError)
    
    with pytest.raises(FileNotFoundError):
        json_reader.read(file_path)

def test_read_permission_error(mocker, json_reader):
    file_path = "restricted_path"

    mocker.patch("builtins.open", side_effect=PermissionError)
    
    with pytest.raises(PermissionError):
        json_reader.read(file_path)
