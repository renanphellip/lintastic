import os
from typing import Any, Dict

from lintastic.core.enums.log_message import LogMessage
from lintastic.utils.logger import Logger

from .file_reader_factory import FileReaderFactory


class FileReaderService:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def read_file(self, file_path: str) -> Dict[str, Any]:
        absolute_file_path = os.path.abspath(file_path.strip())
        if self.verbose:
            Logger.debug(
                LogMessage.READING_FILE.format(file_path=absolute_file_path)
            )
        try:
            file_reader = FileReaderFactory.get_file_reader(absolute_file_path)
            return file_reader.read(absolute_file_path)
        except RecursionError:
            Logger.error(
                LogMessage.CIRCULAR_REFERENCE.format(
                    file_path=absolute_file_path
                )
            )
        except Exception as error:
            Logger.error(
                LogMessage.FAIL_TO_READ_FILE.format(
                    file_path=absolute_file_path, error=error
                )
            )
