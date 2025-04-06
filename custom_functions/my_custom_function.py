from lintastic.core.entities.functions.custom import CustomFunctionInputs


def my_custom_function(
    inputs: CustomFunctionInputs
):
    print(f'This is my custom function. Inputs: {inputs}')
