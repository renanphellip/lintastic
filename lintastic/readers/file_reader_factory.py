from lintastic.enums import LogMessage
from lintastic.readers.file_reader import IFileReader
from lintastic.readers.json_file_reader import JsonFileReader
from lintastic.readers.toml_file_reader import TomlFileReader
from lintastic.readers.yaml_file_reader import YamlFileReader
from lintastic.utils.logger import Logger


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
                LogMessage.UNSUPPORTED_FILE_EXTENSION.format(
                    file_path=file_path
                )
            )
