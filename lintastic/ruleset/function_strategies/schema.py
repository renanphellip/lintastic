from ...entities.spectral import SpectralRuleThen
from ...entities.core.schema import JSONSchemaDraft, SchemaRuleThen, SchemaFunctionOptions

class SchemaFunctionStrategy:
    def set_rule_then(self, spectral_rule_then: SpectralRuleThen):
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
