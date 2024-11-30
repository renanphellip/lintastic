import os
from typing import Literal, Tuple

from lintastic.logs import Logger, LogMessages


class FileValidator:
    @staticmethod
    def validate_extension(
        file_path: str, supported_extensions: Tuple[str], verbose=False
    ) -> Literal[True]:
        if not file_path.lower().endswith(supported_extensions):
            Logger.error(
                LogMessages.INVALID_FILE_EXTENSION.format(
                    file_path=file_path,
                    supported_extensions=supported_extensions,
                )
            )
        if verbose:
            Logger.debug(
                LogMessages.VALID_FILE_EXTENSION.format(file_path=file_path)
            )
        return True

    @staticmethod
    def validate_existence(file_path: str, verbose=False) -> Literal[True]:
        if not os.path.exists(file_path):
            Logger.error(
                LogMessages.FILE_NOT_FOUND.format(file_path=file_path)
            )
        if verbose:
            Logger.debug(LogMessages.FILE_EXISTS.format(file_path=file_path))
        return True
