from typing import Any, Dict, List

from lintastic.enums.log_message import LogMessage
from lintastic.readers.file_reader_service import FileReaderService
from lintastic.utils.logger import Logger


class RefResolveService:
    def __init__(
        self,
        file_reader_service=FileReaderService(),
        verbose=False,
    ):
        self.file_reader_service = file_reader_service
        self.verbose = verbose

    def resolve(self, data: Any, base_path: str) -> Any:
        if isinstance(data, dict):
            return self.__resolve_dict(data, base_path)
        elif isinstance(data, list):
            return self.__resolve_list(data, base_path)
        return data

    # ruff: noqa: PLR6301
    def __is_external_reference(self, key: str, value: Any) -> bool:
        return (
            key == '$ref'
            and isinstance(value, str)
            and not value.startswith('#')
        )

    def __resolve_external_reference(
        self, file_name: str, base_path: str
    ) -> Any:
        file_path = f'{base_path}/{file_name}'
        external_ref_content = self.file_reader_service.read_file(file_path)
        if self.verbose:
            Logger.debug(
                LogMessage.RESOLVING_FILE.format(document_path=file_path)
            )
        data = self.resolve(external_ref_content, base_path)
        return data

    def __resolve_dict(self, data: Dict, base_path: str) -> dict:
        for key, value in data.items():
            if self.__is_external_reference(key, value):
                data = self.__resolve_external_reference(value, base_path)
            else:
                data[key] = self.resolve(value, base_path)
        return data

    def __resolve_list(self, data: List, base_path: str) -> list:
        for i, element in enumerate(data):
            data[i] = self.resolve(element, base_path)
        return data
