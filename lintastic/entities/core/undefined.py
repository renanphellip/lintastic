from pydantic import BaseModel


class UndefinedRuleThen(BaseModel):
    field: str
    function: str = 'undefined'
