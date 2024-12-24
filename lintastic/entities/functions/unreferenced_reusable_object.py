from pydantic import BaseModel

from lintastic.enums import CoreFunction


class UnreferencedReusableObjectFunctionOptions(BaseModel):
    reusable_objects_location: str


class UnreferencedReusableObjectRuleThen(BaseModel):
    function: CoreFunction = CoreFunction.UNREFERENCED_REUSABLE_OBJECT
    function_options: UnreferencedReusableObjectFunctionOptions
