import os

from lintastic.entities.diagnostic import DiagnosticCollection
from lintastic.enums.log_message import LogMessage
from lintastic.utils.logger import Logger


class TxtFileWriter:
    # ruff: noqa: PLR6301
    def write(
        self, output_path: str, diagnostic_collection: DiagnosticCollection
    ) -> str:
        absolute_output_path = os.path.abspath(output_path.strip())
        if not isinstance(diagnostic_collection, DiagnosticCollection):
            Logger.error(
                LogMessage.FAIL_TO_WRITE_FILE_WITH_INVALID_TYPE.format(
                    output_path=absolute_output_path
                )
            )
        with open(absolute_output_path, 'w', encoding='utf-8') as file:
            for diagnostic in diagnostic_collection.diagnostics:
                file.write(f'Rule: {diagnostic.rule}\n')
                file.write(f'Severity: {diagnostic.severity}\n')
                file.write(f'Context: {diagnostic.context}\n')
                file.write('Messages:\n')
                for message in diagnostic.messages:
                    file.write(f'- {message}\n')
                if diagnostic.documentations:
                    file.write('Documentations:\n')
                    for doc in diagnostic.documentations:
                        file.write(f'- {doc}\n')
                file.write('\n')
            file.write('Summary:\n')
            file.write(
                '- Total errors: '
                + diagnostic_collection.summary.total_errors
                + '\n'
            )
            file.write(
                '- Total warnings: '
                + diagnostic_collection.summary.total_warnings
                + '\n'
            )
            file.write(
                '- Total informations: '
                + diagnostic_collection.summary.total_informations
                + '\n'
            )
            file.write(
                '- Total hints: '
                + diagnostic_collection.summary.total_hints
                + '\n'
            )
        return absolute_output_path
