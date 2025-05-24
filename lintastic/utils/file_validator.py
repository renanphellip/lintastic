import os
from enum import Enum

from lintastic.core.enums.log_message import LogMessage


class FileValidator:
    @staticmethod
    def validate_extension(file_path: str, supported_extensions: Enum) -> tuple[bool, str]:
        valid_extensions = [ext.value for ext in supported_extensions]
        valid_extension = file_path.lower().endswith(tuple(valid_extensions))
        if not valid_extension:
            return False, LogMessage.INVALID_FILE_EXTENSION.format(
                file_path=file_path,
                supported_extensions=valid_extensions,
            )
        return True, ''

    @staticmethod
    def validate_existence(file_path: str) -> tuple[bool, str]:
        if not os.path.exists(file_path):
            return False, LogMessage.FILE_NOT_FOUND.format(file_path=file_path)
        return True, ''
