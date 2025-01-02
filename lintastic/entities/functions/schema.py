from typing import Any, Dict

from pydantic import BaseModel, Field

from lintastic.enums.core_function import CoreFunction
from lintastic.enums.json_schema import JSONSchemaDraft


class SchemaFunctionOptions(BaseModel):
    schema_definition: Dict[str, Any] = Field(..., alias='schema')
    dialect: JSONSchemaDraft = JSONSchemaDraft.AUTO
    all_errors: bool = False


class SchemaRuleThen(BaseModel):
    field: str
    function: CoreFunction = CoreFunction.SCHEMA
    function_options: SchemaFunctionOptions
