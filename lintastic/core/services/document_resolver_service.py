from pathlib import Path
from typing import Any, Dict

from rich.markup import escape

from lintastic.core.enums.log_message import LogMessage
from lintastic.core.interfaces.document_resolver_service import IDocumentResolverService
from lintastic.core.interfaces.ref_resolver_service import IRefResolverService
from lintastic.io.interfaces.file_reader_service import IFileReaderService
from lintastic.utils.logger import Logger


class DocumentResolverService(IDocumentResolverService):
    def __init__(
        self,
        file_reader_service: IFileReaderService,
        ref_resolver_service: IRefResolverService,
    ):
        super().__init__(file_reader_service, ref_resolver_service)

    def resolve(self, document_path: str) -> Dict[str, Any]:
        try:
            document_base_path = Path(document_path).parent
            document_data = self.file_reader_service.read_file(document_path)

            Logger.debug(LogMessage.RESOLVING_FILE.format(document_path=document_path))

            resolved_document_data = self.ref_resolver_service.resolve(document_data, document_base_path)
            return resolved_document_data

        except Exception as error:
            escaped_error = escape(str(error))
            Logger.error(LogMessage.FAIL_TO_RESOLVE_FILE.format(document_path=document_path, error=escaped_error))
