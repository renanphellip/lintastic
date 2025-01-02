from lintastic.enums.log_message import LogMessage
from lintastic.utils.logger import Logger

from .file_reader import IFileReader
from .json_file_reader import JsonFileReader
from .toml_file_reader import TomlFileReader
from .yaml_file_reader import YamlFileReader


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
