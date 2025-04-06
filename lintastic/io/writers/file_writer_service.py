import os
from typing import Any

from lintastic.core.enums.log_message import LogMessage
from lintastic.utils.logger import Logger

from .file_writer_factory import FileWriterFactory


class FileWriterService:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __create_output_directory(self, output_path: str) -> None:
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            if self.verbose:
                Logger.debug(
                    LogMessage.CREATING_DIRECTORY.format(output_dir=output_dir)
                )
            os.makedirs(output_dir)

    def write_file(self, output_path: str, data: Any) -> str:
        try:
            self.__create_output_directory(output_path)
            absolute_output_path = os.path.abspath(output_path.strip())
            if self.verbose:
                Logger.debug(
                    LogMessage.CREATING_OUTPUT_FILE.format(
                        output_path=absolute_output_path
                    )
                )
            file_writer = FileWriterFactory.get_file_writer(
                absolute_output_path
            )
            absolute_output_path = file_writer.write(output_path, data)
            return absolute_output_path
        except Exception as error:
            Logger.error(
                LogMessage.FAIL_TO_CREATE.format(
                    output_path=absolute_output_path, error=error
                )
            )
