from lintastic.file_reader.file_reader import IFileReader
from lintastic.file_reader.json_file_reader import JsonFileReader
from lintastic.file_reader.toml_file_reader import TomlFileReader
from lintastic.file_reader.yaml_file_reader import YamlFileReader
from lintastic.logs import Logger, LogMessages


class FileReaderFactory:
    @staticmethod
    def get_file_reader(file_path: str) -> IFileReader:
        file_path = file_path.lower()
        if file_path.endswith('.toml'):
            return TomlFileReader()
        elif file_path.endswith('.json'):
            return JsonFileReader()
        elif file_path.endswith(('yaml', 'yml')):
            return YamlFileReader()
        else:
            Logger.error(
                LogMessages.UNSUPPORTED_FILE_EXTENSION.format(
                    file_path=file_path
                )
            )
