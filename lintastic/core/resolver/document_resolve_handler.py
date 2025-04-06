from pathlib import Path
from typing import Any, Dict

from rich.markup import escape

from lintastic.core.enums.log_message import LogMessage
from lintastic.core.resolver.ref_resolve_service import RefResolveService
from lintastic.io.readers.file_reader_service import FileReaderService
from lintastic.utils.logger import Logger


class DocumentResolveHandler:
    def __init__(
        self,
        verbose=False,
    ):
        self.verbose = verbose
        self.file_reader_service = FileReaderService(verbose)
        self.ref_resolve_service = RefResolveService(
            self.file_reader_service, verbose
        )

    def resolve(self, document_path: str) -> Dict[str, Any]:
        try:
            document_base_path = Path(document_path).parent
            document_data = self.file_reader_service.read_file(document_path)

            if self.verbose:
                Logger.debug(
                    LogMessage.RESOLVING_FILE.format(
                        document_path=document_path
                    )
                )

            resolved_document_data = self.ref_resolve_service.resolve(
                document_data, document_base_path
            )
            return resolved_document_data

        except Exception as error:
            escaped_error = escape(str(error))
            Logger.error(
                LogMessage.FAIL_TO_RESOLVE_FILE.format(
                    document_path=document_path, error=escaped_error
                )
            )
