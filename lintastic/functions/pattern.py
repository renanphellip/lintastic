import re
from typing import List

from lintastic.entities.functions.pattern import PatternFunctionOptions


def pattern(
    context: str,
    target_value: str,
    function_options: PatternFunctionOptions,
    verbose: bool,
    rule_name: str,
) -> List[str]:
    regex_match = function_options.match
    regex_not_match = function_options.not_match
    messages = []
    if isinstance(regex_match, str) and len(regex_match) > 0:
        if not re.match(rf'{regex_match}', target_value):
            messages.append(f'{context} must match this regex: {regex_match}')
    if isinstance(regex_not_match, str) and len(regex_not_match) > 0:
        if re.match(rf'{regex_not_match}', target_value):
            messages.append(
                f'{context} must not match this regex: {regex_not_match}'
            )
    return messages
