import os
from typing import Any, Dict

from lintastic.core.enums.log_message import LogMessage
from lintastic.io.interfaces.file_reader_service import IFileReaderService
from lintastic.utils.logger import Logger

from .file_reader_factory import FileReaderFactory


class FileReaderService(IFileReaderService):
    @staticmethod
    def read_file(file_path: str) -> Dict[str, Any]:
        absolute_file_path = os.path.abspath(file_path.strip())
        Logger.debug(LogMessage.READING_FILE.format(file_path=absolute_file_path))
        try:
            file_reader = FileReaderFactory.get_file_reader(absolute_file_path)
            return file_reader.read(absolute_file_path)
        except RecursionError:
            Logger.error(LogMessage.CIRCULAR_REFERENCE.format(file_path=absolute_file_path))
        except Exception as error:
            Logger.error(LogMessage.FAIL_TO_READ_FILE.format(file_path=absolute_file_path, error=error))
