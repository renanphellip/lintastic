from pydantic import BaseModel


class FalsyRuleThen(BaseModel):
    field: str
    function: str = 'falsy'
