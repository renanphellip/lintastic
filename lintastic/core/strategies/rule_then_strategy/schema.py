from lintastic.core.entities.functions.schema import (
    JSONSchemaDraft,
    SchemaFunctionOptions,
    SchemaRuleThen,
)
from lintastic.core.entities.spectral import SpectralRuleThen
from lintastic.core.interfaces.rule_then_strategy import IRuleThenStrategy


class SchemaRuleThenStrategy(IRuleThenStrategy):
    @staticmethod
    def set_rule_then(spectral_rule_then: SpectralRuleThen, rule_name: str):
        return SchemaRuleThen(
            field=spectral_rule_then.field,
            function_options=SchemaFunctionOptions(
                schema_definition=spectral_rule_then.functionOptions.get('schema'),
                dialect=spectral_rule_then.functionOptions.get('dialect', JSONSchemaDraft.AUTO),
                all_errors=spectral_rule_then.functionOptions.get('allErrors', False),
            ),
        )
