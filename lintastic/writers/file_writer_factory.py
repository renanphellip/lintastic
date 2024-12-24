from lintastic.enums import LogMessage
from lintastic.utils.logger import Logger
from lintastic.writers.file_writer import IFileWriter
from lintastic.writers.json_file_writer import JsonFileWriter
from lintastic.writers.txt_file_writer import TxtFileWriter
from lintastic.writers.yaml_file_writer import YamlFileWriter


class FileWriterFactory:
    @staticmethod
    def get_file_writer(output_path: str) -> IFileWriter:
        output_path = output_path.lower()
        if output_path.endswith('.txt'):
            return TxtFileWriter()
        elif output_path.endswith('.json'):
            return JsonFileWriter()
        elif output_path.endswith(('yaml', 'yml')):
            return YamlFileWriter()
        else:
            Logger.error(
                LogMessage.UNSUPPORTED_FILE_EXTENSION.format(
                    file_path=output_path
                )
            )
