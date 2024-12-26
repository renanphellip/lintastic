from typing import Any, Dict

from lintastic.readers.file_reader_service import FileReaderService
from lintastic.resolver.document_resolve_handler import DocumentResolveHandler


class DocumentDataLoader:
    def __init__(self, document_path: str, verbose=False):
        self.document_path = document_path
        self.verbose = verbose

    def load(self, resolve_refs: bool) -> Dict[str, Any]:
        if resolve_refs:
            return DocumentResolveHandler(self.verbose).resolve(
                self.document_path
            )
        return FileReaderService(self.verbose).read_file(self.document_path)
