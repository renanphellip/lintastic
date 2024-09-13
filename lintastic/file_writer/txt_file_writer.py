import os
from typing import Any

from lintastic.entities.validator import ValidationResultCollection


class TxtFileWriter:
    def write(self, output_path: str, data: Any) -> str:
        if not isinstance(data, ValidationResultCollection):
            raise TypeError(
                'Data must be an instance of ValidationResultCollection.'
            )
        absolute_output_path = os.path.abspath(output_path.strip())
        with open(absolute_output_path, 'w', encoding='utf-8') as file:
            for validation_result in data.validation_results:
                file.write(f'Rule: {validation_result.rule}\n')
                file.write(f'Context: {validation_result.context}\n')
                file.write(f'Severity: {validation_result.severity}\n')
                file.write('Messages:\n')
                for message in validation_result.messages:
                    file.write(f'- {message}\n')
                if validation_result.documentations:
                    file.write('Documentations:\n')
                    for doc in validation_result.documentations:
                        file.write(f'- {doc}\n')
                file.write('\n')
            file.write(
                f'Total errors: {data.validation_summary.total_errors}\n'
            )
            file.write(
                f'Total warnings: {data.validation_summary.total_warnings}\n'
            )
            file.write(
                'Total informations: '
                f'{data.validation_summary.total_warnings}\n'
            )
            file.write(
                f'Total hints: {data.validation_summary.total_warnings}\n'
            )
        return absolute_output_path
