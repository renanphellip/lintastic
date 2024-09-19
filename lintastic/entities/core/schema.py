from enum import Enum
from typing import Any, Dict

from pydantic import BaseModel, Field


class JSONSchemaDraft(str, Enum):
    AUTO = 'auto'
    DRAFT4 = 'draft4'
    DRAFT6 = 'draft6'
    DRAFT7 = 'draft7'
    DRAFT201909 = 'draft2019-09'
    DRAFT202012 = 'draft2020-12'

    def __str__(self):
        return self.value


class SchemaFunctionOptions(BaseModel):
    schema_definition: Dict[str, Any] = Field(..., alias='schema')
    dialect: JSONSchemaDraft = JSONSchemaDraft.AUTO
    all_errors: bool = False


class SchemaRuleThen(BaseModel):
    field: str
    function: str = 'schema'
    function_options: SchemaFunctionOptions
