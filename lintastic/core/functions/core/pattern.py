import re
from typing import List

from lintastic.core.entities.functions.pattern import PatternFunctionInputs


def pattern(inputs: PatternFunctionInputs) -> List[str]:
    regex_match = inputs.options.match
    regex_not_match = inputs.options.not_match
    messages = []
    if isinstance(regex_match, str) and len(regex_match) > 0:
        if not re.match(rf'{regex_match}', inputs.target_value):
            messages.append(
                f'{inputs.context} must match this regex: {regex_match}'
            )
    if isinstance(regex_not_match, str) and len(regex_not_match) > 0:
        if re.match(rf'{regex_not_match}', inputs.target_value):
            messages.append(
                f'{inputs.context} must not match this regex: '
                + regex_not_match
            )
    return messages
