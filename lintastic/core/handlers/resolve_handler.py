import os

from lintastic.cli.dto.resolve_inputs_dto import ResolveInputsDTO
from lintastic.core.enums.log_message import LogMessage
from lintastic.core.services.document_resolver_service import (
    DocumentResolverService,
)
from lintastic.core.services.ref_resolver_service import RefResolverService
from lintastic.io.readers.file_reader_service import FileReaderService
from lintastic.io.writers.file_writer_service import FileWriterService
from lintastic.utils.logger import Logger


class ResolveHandler:
    @staticmethod
    def execute(inputs: ResolveInputsDTO) -> None:
        # Verbose
        if inputs.verbose:
            os.environ['LINTASTIC_VERBOSE'] = 'true'

        # Resolve
        file_reader_service = FileReaderService()
        ref_resolver_service = RefResolverService(file_reader_service)
        document_resolver_service = DocumentResolverService(file_reader_service, ref_resolver_service)
        resolved_document_data = document_resolver_service.resolve(inputs.document_path)

        # Output
        file_writer_service = FileWriterService()
        absolute_output_path = file_writer_service.write_file(inputs.output_path, resolved_document_data)
        Logger.success(LogMessage.DOCUMENT_RESOLVED.format(resolved_document_path=absolute_output_path))
