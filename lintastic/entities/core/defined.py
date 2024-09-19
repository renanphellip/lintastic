from pydantic import BaseModel


class DefinedRuleThen(BaseModel):
    field: str
    function: str = 'defined'
