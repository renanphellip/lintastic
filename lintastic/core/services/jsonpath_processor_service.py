import json
from typing import Any, Dict, List

from jsonpath_ng import parse
from rich.markup import escape

from lintastic.core.entities.jsonpath_match import JSONPathMatch
from lintastic.core.entities.rule import Rule
from lintastic.core.enums.log_message import LogMessage
from lintastic.core.interfaces.jsonpath_processor_service import IJSONPathProcessorService
from lintastic.utils.logger import Logger


class JSONPathProcessorService(IJSONPathProcessorService):
    def __init__(self, document_data: Dict[str, Any]):
        super().__init__(document_data)

    def process(self, rule: Rule) -> List[JSONPathMatch]:
        results = []
        for jsonpath in rule.given:
            results.extend(self._validate_each_jsonpath_given(jsonpath))
        return results

    def _validate_each_jsonpath_given(self, jsonpath_given: str) -> List[JSONPathMatch]:
        try:
            naming_filter = jsonpath_given.endswith('~')
            jsonpath_given = jsonpath_given[:-1] if naming_filter else jsonpath_given
            pattern = parse(jsonpath_given)
            root_string = '' if jsonpath_given == '$' else '$.'
            results = [
                JSONPathMatch(
                    context=root_string + str(match.full_path),
                    target_value=str(match.path) if naming_filter else match.value,
                )
                for match in pattern.find(self.document_data)
            ]
            results_json_string = json.dumps([result.__dict__ for result in results])
            Logger.debug(
                LogMessage.JSONPATH_RESULTS.format(
                    jsonpath_given=jsonpath_given,
                    jsonpath_results=results_json_string,
                )
            )
            return results
        except Exception as error:
            escaped_jsonpath_given = escape(str(jsonpath_given))
            escaped_error = escape(str(error))
            Logger.error(
                LogMessage.FAIL_TO_PARSE_JSONPATH.format(
                    jsonpath_given=escaped_jsonpath_given,
                    error=escaped_error,
                ),
                exit_program=False,
            )
