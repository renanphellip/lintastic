from lintastic.enums import LogMessage
from lintastic.utils import Logger
from lintastic.writers import (
    IFileWriter,
    JsonFileWriter,
    MdFileWriter,
    TxtFileWriter,
    YamlFileWriter,
)


class FileWriterFactory:
    @staticmethod
    def get_file_writer(output_path: str) -> IFileWriter:
        output_path = output_path.lower()
        if output_path.endswith('.txt'):
            return TxtFileWriter()
        elif output_path.endswith('.md'):
            return MdFileWriter()
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
