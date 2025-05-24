from abc import ABC, abstractmethod
from typing import Any, Dict

from lintastic.core.interfaces.ref_resolver_service import IRefResolverService
from lintastic.io.interfaces.file_reader_service import IFileReaderService


class IDocumentResolverService(ABC):
    def __init__(
        self,
        file_reader_service: IFileReaderService,
        ref_resolver_service: IRefResolverService,
    ):
        self.file_reader_service = file_reader_service
        self.ref_resolver_service = ref_resolver_service

    @abstractmethod
    def resolve(self, document_path: str) -> Dict[str, Any]:
        pass
