from typing import Any, Dict, List

from jsonpath_ng import parse
from rich.markup import escape

from lintastic.entities.jsonpath import JSONPathMatch
from lintastic.enums import LogMessage
from lintastic.utils.logger import Logger


class JSONPathValidator:
    def __init__(
        self,
        jsonpath_pattern: str,
        document_data: Dict[str, Any],
        verbose=False,
    ):
        self.verbose = verbose
        self.naming_filter = jsonpath_pattern.endswith('~')
        self.jsonpath_pattern = self.__process_jsonpath_pattern(
            jsonpath_pattern
        )
        self.document_data = document_data

    def __process_jsonpath_pattern(self, jsonpath_pattern: str) -> str:
        jsonpath_pattern = (
            jsonpath_pattern[:-1] if self.naming_filter else jsonpath_pattern
        )
        return jsonpath_pattern

    def validate(self) -> List[JSONPathMatch]:
        try:
            pattern = parse(self.jsonpath_pattern)
            root_string = '' if self.jsonpath_pattern == '$' else '$.'
            results = [
                JSONPathMatch(
                    context=root_string + str(match.full_path),
                    target_value=str(match.path)
                    if self.naming_filter
                    else match.value,
                )
                for match in pattern.find(self.document_data)
            ]
            if self.verbose:
                results_len = len(results)
                Logger.debug(
                    LogMessage.JSONPATH_RESULTS_LENGTH.format(
                        results_len=results_len,
                        jsonpath_pattern=self.jsonpath_pattern,
                    )
                )
            return results
        except Exception as error:
            escaped_jsonpath_pattern = escape(str(self.jsonpath_pattern))
            escaped_error = escape(str(error))
            Logger.error(
                LogMessage.FAIL_TO_PARSE_JSONPATH.format(
                    jsonpath_pattern=escaped_jsonpath_pattern,
                    error=escaped_error,
                )
            )