from pydantic import BaseModel

from lintastic.enums import CoreFunction


class PatternFunctionOptions(BaseModel):
    match: str = ''
    not_match: str = ''


class PatternRuleThen(BaseModel):
    function: CoreFunction = CoreFunction.PATTERN
    function_options: PatternFunctionOptions
