from typing import Any, Dict, List

from lintastic.core.entities.jsonpath import JSONPathMatch
from lintastic.core.entities.rule import Rule
from lintastic.core.validators.jsonpath_validator import JSONPathValidator


class JSONPathProcessor:
    @staticmethod
    def process(
        rule: Rule, document_data: Dict[str, Any], verbose=False
    ) -> List[JSONPathMatch]:
        results = []
        for jsonpath in rule.given:
            results.extend(
                JSONPathValidator(jsonpath, document_data, verbose).validate()
            )
        return results
