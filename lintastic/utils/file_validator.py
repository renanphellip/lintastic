import os
from enum import Enum
from typing import Literal

from lintastic.enums import LogMessage
from lintastic.utils import Logger


class FileValidator:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def validate_extension(
        self, file_path: str, supported_extensions: Enum
    ) -> Literal[True]:
        extensions_list = [ext.value for ext in supported_extensions]
        is_valid_extension = file_path.lower().endswith(tuple(extensions_list))
        if not is_valid_extension:
            Logger.error(
                LogMessage.INVALID_FILE_EXTENSION.format(
                    file_path=file_path,
                    supported_extensions=extensions_list,
                )
            )
        if self.verbose:
            Logger.debug(
                LogMessage.VALID_FILE_EXTENSION.format(file_path=file_path)
            )
        return True

    def validate_existence(self, file_path: str) -> Literal[True]:
        if not os.path.exists(file_path):
            Logger.error(LogMessage.FILE_NOT_FOUND.format(file_path=file_path))
        if self.verbose:
            Logger.debug(LogMessage.FILE_EXISTS.format(file_path=file_path))
        return True
