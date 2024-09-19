from pydantic import BaseModel


class PatternFunctionOptions(BaseModel):
    match: str = ''
    not_match: str = ''


class PatternRuleThen(BaseModel):
    function: str = 'pattern'
    function_options: PatternFunctionOptions
