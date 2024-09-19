from pydantic import BaseModel


class AlphabeticalFunctionOptions(BaseModel):
    keyed_by: str


class AlphabeticalRuleThen(BaseModel):
    field: str
    function: str = 'alphabetical'
    function_options: AlphabeticalFunctionOptions
