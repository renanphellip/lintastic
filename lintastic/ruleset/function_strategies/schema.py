from lintastic.entities.functions.schema import (
    JSONSchemaDraft,
    SchemaFunctionOptions,
    SchemaRuleThen,
)
from lintastic.entities.spectral import SpectralRuleThen


class SchemaFunctionStrategy:
    # ruff: noqa: PLR6301
    def set_rule_then(
        self, spectral_rule_then: SpectralRuleThen, rule_name: str
    ):
        return SchemaRuleThen(
            field=spectral_rule_then.field,
            function_options=SchemaFunctionOptions(
                schema_definition=spectral_rule_then.functionOptions.get(
                    'schema'
                ),
                dialect=spectral_rule_then.functionOptions.get(
                    'dialect', JSONSchemaDraft.AUTO
                ),
                all_errors=spectral_rule_then.functionOptions.get(
                    'allErrors', False
                ),
            ),
        )
