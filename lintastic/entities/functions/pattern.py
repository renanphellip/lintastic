from pydantic import BaseModel

from lintastic.enums.core_function import CoreFunction


class PatternFunctionOptions(BaseModel):
    match: str = ''
    not_match: str = ''


class PatternRuleThen(BaseModel):
    function: CoreFunction = CoreFunction.PATTERN
    function_options: PatternFunctionOptions
