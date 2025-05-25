from lintastic.core.enums.log_message import LogMessage
from lintastic.io.interfaces.file_writer import IFileWriter
from lintastic.utils.logger import Logger

from .json_file_writer import JsonFileWriter
from .md_file_writer import MdFileWriter
from .txt_file_writer import TxtFileWriter
from .yaml_file_writer import YamlFileWriter


class FileWriterFactory:
    @staticmethod
    def get_file_writer(output_path: str) -> IFileWriter:
        output_path = output_path.lower()
        if output_path.endswith('.json'):
            return JsonFileWriter()
        elif output_path.endswith('.md'):
            return MdFileWriter()
        elif output_path.endswith('.txt'):
            return TxtFileWriter()
        elif output_path.endswith(('yaml', 'yml')):
            return YamlFileWriter()
        else:
            Logger.error(LogMessage.UNSUPPORTED_FILE_EXTENSION.format(file_path=output_path))
