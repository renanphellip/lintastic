import os
from typing import Any

from lintastic.core.enums.log_message import LogMessage
from lintastic.io.interfaces.file_writer_service import IFileWriterService
from lintastic.utils.logger import Logger

from .file_writer_factory import FileWriterFactory


class FileWriterService(IFileWriterService):
    @staticmethod
    def _create_output_directory(output_path: str) -> None:
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            Logger.debug(LogMessage.CREATING_DIRECTORY.format(output_dir=output_dir))
            os.makedirs(output_dir)

    @staticmethod
    def write_file(output_path: str, data: Any) -> str:
        try:
            FileWriterService._create_output_directory(output_path)
            absolute_output_path = os.path.abspath(output_path.strip())
            Logger.debug(LogMessage.CREATING_OUTPUT_FILE.format(output_path=absolute_output_path))
            file_writer = FileWriterFactory.get_file_writer(absolute_output_path)
            absolute_output_path = file_writer.write(output_path, data)
            return absolute_output_path
        except Exception as error:
            Logger.error(LogMessage.FAIL_TO_CREATE.format(output_path=absolute_output_path, error=error))
