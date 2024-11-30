from lintastic.file_writer.file_writer import IFileWriter
from lintastic.file_writer.json_file_writer import JsonFileWriter
from lintastic.file_writer.txt_file_writer import TxtFileWriter
from lintastic.file_writer.yaml_file_writer import YamlFileWriter
from lintastic.logs import Logger, LogMessages


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
                LogMessages.UNSUPPORTED_FILE_EXTENSION.format(
                    file_path=output_path
                )
            )
