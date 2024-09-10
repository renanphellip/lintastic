import yaml
import pytest
from lintastic.file_reader.yaml_file_reader import YamlFileReader


@pytest.fixture
def yaml_reader():
    return YamlFileReader()

def test_read_yaml(mocker, yaml_reader):
    yaml_content = "key: value"
    expected_result = {"key": "value"}
    file_path = "dummy_path"
    
    mocker.patch("builtins.open", mocker.mock_open(read_data=yaml_content))
    
    result = yaml_reader.read(file_path)
    assert result == expected_result

def test_read_file_not_found(mocker, yaml_reader):
    file_path = "non_existent_path"

    mocker.patch("builtins.open", side_effect=FileNotFoundError)
    
    with pytest.raises(FileNotFoundError):
        yaml_reader.read(file_path)

def test_read_permission_error(mocker, yaml_reader):
    file_path = "restricted_path"

    mocker.patch("builtins.open", side_effect=PermissionError)
    
    with pytest.raises(PermissionError):
        yaml_reader.read(file_path)
