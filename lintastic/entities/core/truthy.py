from pydantic import BaseModel


class TruthyRuleThen(BaseModel):
    field: str
    function: str = 'truthy'
