from abc import ABC, abstractmethod
from typing import Any

from lintastic.io.interfaces.file_reader_service import IFileReaderService


class IRefResolverService(ABC):
    def __init__(
        self,
        file_reader_service: IFileReaderService,
    ):
        self.file_reader_service = file_reader_service

    @abstractmethod
    def resolve(self, data: Any, base_path: str) -> Any:
        pass
