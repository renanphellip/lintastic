from pydantic import BaseModel


class UnreferencedReusableObjectFunctionOptions(BaseModel):
    reusable_objects_location: str


class UnreferencedReusableObjectRuleThen(BaseModel):
    function: str = 'unreferencedReusableObject'
    function_options: UnreferencedReusableObjectFunctionOptions
