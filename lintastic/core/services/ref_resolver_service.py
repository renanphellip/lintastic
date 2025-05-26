from typing import Any, Dict, List

from lintastic.core.enums.log_message import LogMessage
from lintastic.core.interfaces.ref_resolver_service import IRefResolverService
from lintastic.io.interfaces.file_reader_service import IFileReaderService
from lintastic.utils.logger import Logger


class RefResolverService(IRefResolverService):
    def __init__(self, file_reader_service: IFileReaderService):
        super().__init__(file_reader_service)

    def resolve(self, data: Any, base_path: str) -> Any:
        if isinstance(data, dict):
            return self._resolve_dict(data, base_path)
        elif isinstance(data, list):
            return self._resolve_list(data, base_path)
        return data

    @staticmethod
    def _is_external_reference(key: str, value: Any) -> bool:
        return key == '$ref' and isinstance(value, str) and not value.startswith('#')

    def _resolve_external_reference(self, file_name: str, base_path: str) -> Any:
        file_path = f'{base_path}/{file_name}'
        external_ref_content = self.file_reader_service.read_file(file_path)
        Logger.debug(LogMessage.RESOLVING_FILE.format(document_path=file_path))
        data = self.resolve(external_ref_content, base_path)
        return data

    def _resolve_dict(self, data: Dict, base_path: str) -> dict:
        for key, value in data.items():
            if self._is_external_reference(key, value):
                data = self._resolve_external_reference(value, base_path)
            else:
                data[key] = self.resolve(value, base_path)
        return data

    def _resolve_list(self, data: List, base_path: str) -> list:
        for i, element in enumerate(data):
            data[i] = self.resolve(element, base_path)
        return data
