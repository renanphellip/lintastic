import os

from lintastic.entities.diagnostic import DiagnosticCollection
from lintastic.enums.log_message import LogMessage
from lintastic.utils.logger import Logger


class MdFileWriter:
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
            if diagnostic_collection.diagnostics:
                file.write('## Diagnostics\n\n')
                file.write(
                    '| Rule | Severity | Context | Messages '
                    '| Documentations |\n'
                )
                file.write('| - | - | - | - | - |\n')
                for diagnostic in diagnostic_collection.diagnostics:
                    diagnostic_messages = ''.join(
                        f'- {message}<br>' for message in diagnostic.messages
                    )
                    diagnostic_docs = ''.join(
                        f'- {doc}<br>' for doc in diagnostic.documentations
                    )
                    file.write(
                        f'| {diagnostic.rule} | {diagnostic.severity} | '
                        f'{diagnostic.context} | {diagnostic_messages} | '
                        f'{diagnostic_docs} |\n'
                    )
            file.write('\n### Summary\n\n')
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
