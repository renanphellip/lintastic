import re
from typing import List

from lintastic.entities.functions.inputs import FunctionInputs


def _is_flat_case(
    input: str,
    disallow_digits: bool,
    separator_char: str,
    separator_allow_leading: bool,
) -> bool:
    regex = r''
    if disallow_digits is True:
        regex = r'[a-z]+'
        if separator_char:
            regex = rf'[a-z]+(?:{separator_char}[a-z]+)*'
            if separator_allow_leading is True:
                regex = rf'{separator_char}?[a-z]+(?:{separator_char}[a-z]+)*'
    else:
        regex = r'[a-z]+[a-z0-9]*'
        if separator_char:
            regex = rf'[a-z]+[a-z0-9]*(?:{separator_char}[a-z]+[a-z0-9]*)*'
            if separator_allow_leading is True:
                regex = (
                    rf'{separator_char}?[a-z]+[a-z0-9]*'
                    rf'(?:{separator_char}[a-z]+[a-z0-9]*)*'
                )
    return bool(re.match(rf'^{regex}$', input))


def _is_camel_case(
    input: str,
    disallow_digits: bool,
    separator_char: str,
    separator_allow_leading: bool,
) -> bool:
    regex = r''
    if disallow_digits is True:
        regex = r'[a-z]+(?:[A-Z][a-z]+)*'
        if separator_char:
            regex = (
                rf'[a-z]+(?:[A-Z][a-z]+)*'
                rf'(?:{separator_char}?[a-z]+(?:[A-Z][a-z]+)*)*'
            )
            if separator_allow_leading is True:
                regex = (
                    rf'{separator_char}?[a-z]+'
                    rf'(?:[A-Z][a-z]+)*(?:{separator_char}?[a-z]+'
                    rf'(?:[A-Z][a-z]+)*)*'
                )
    else:
        regex = r'[a-z]+(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*'
        if separator_char:
            regex = (
                rf'[a-z]+(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*'
                rf'(?:{separator_char}?[a-z]+'
                rf'(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*)*'
            )
            if separator_allow_leading is True:
                regex = (
                    rf'{separator_char}?[a-z]+'
                    rf'(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*'
                    rf'(?:{separator_char}?[a-z]+'
                    rf'(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*)*'
                )
    return bool(re.match(rf'^{regex}$', input))


def _is_pascal_case(
    input: str,
    disallow_digits: bool,
    separator_char: str,
    separator_allow_leading: bool,
) -> bool:
    regex = r''
    if disallow_digits is True:
        regex = r'[A-Z][a-z]+(?:[A-Z][a-z]+)*'
        if separator_char:
            regex = (
                rf'[A-Z][a-z]+(?:[A-Z][a-z]+)*'
                rf'(?:{separator_char}?[A-Z][a-z]+(?:[A-Z][a-z]+)*)*'
            )
            if separator_allow_leading is True:
                regex = (
                    rf'{separator_char}?[A-Z][a-z]+(?:[A-Z][a-z]+)*'
                    rf'(?:{separator_char}?[A-Z][a-z]+(?:[A-Z][a-z]+)*)*'
                )
    else:
        regex = r'[A-Z][a-z]+(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*'
        if separator_char:
            regex = (
                rf'[A-Z][a-z]+(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*'
                rf'(?:{separator_char}?[A-Z][a-z]+'
                rf'(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*)*'
            )
            if separator_allow_leading is True:
                regex = (
                    rf'{separator_char}?[A-Z][a-z]+'
                    rf'(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*'
                    rf'(?:{separator_char}?[A-Z][a-z]+'
                    rf'(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*)*'
                )
    return bool(re.match(rf'^{regex}$', input))


def _is_kebab_case(
    input: str,
    disallow_digits: bool,
    separator_char: str,
    separator_allow_leading: bool,
) -> bool:
    regex = r''
    if disallow_digits is True:
        regex = r'[a-z]+(?:-[a-z]+)*'
        if separator_char:
            regex = (
                rf'[a-z]+(?:-[a-z]+)*(?:{separator_char}?[a-z]+(?:-[a-z]+)*)*'
            )
            if separator_allow_leading is True:
                regex = (
                    rf'{separator_char}?[a-z]+(?:-[a-z]+)*'
                    rf'(?:{separator_char}?[a-z]+(?:-[a-z]+)*)*'
                )
    else:
        regex = r'[a-z]+(?:-[a-z0-9]+)*'
        if separator_char:
            regex = (
                rf'[a-z]+(?:-[a-z0-9]+)*'
                rf'(?:{separator_char}?[a-z]+(?:-[a-z0-9]+)*)*'
            )
            if separator_allow_leading is True:
                regex = (
                    rf'{separator_char}?[a-z]+(?:-[a-z0-9]+)*'
                    rf'(?:{separator_char}?[a-z]+(?:-[a-z0-9]+)*)*'
                )
    return bool(re.match(rf'^{regex}$', input))


def _is_cobol_case(
    input: str,
    disallow_digits: bool,
    separator_char: str,
    separator_allow_leading: bool,
) -> bool:
    regex = r''
    if disallow_digits is True:
        regex = r'[A-Z]+(?:-[A-Z]+)*'
        if separator_char:
            regex = (
                rf'[A-Z]+(?:-[A-Z]+)*(?:{separator_char}?[A-Z]+(?:-[A-Z]+)*)*'
            )
            if separator_allow_leading is True:
                regex = (
                    rf'{separator_char}?[A-Z]+(?:-[A-Z]+)*'
                    rf'(?:{separator_char}?[A-Z]+(?:-[A-Z]+)*)*'
                )
    else:
        regex = r'[A-Z]+(?:-[A-Z0-9]+)*'
        if separator_char:
            regex = (
                rf'[A-Z]+(?:-[A-Z0-9]+)*(?:{separator_char}?[A-Z]+'
                rf'(?:-[A-Z0-9]+)*)*'
            )
            if separator_allow_leading is True:
                regex = (
                    rf'{separator_char}?[A-Z]+(?:-[A-Z0-9]+)*'
                    rf'(?:{separator_char}?[A-Z]+(?:-[A-Z0-9]+)*)*'
                )
    return bool(re.match(rf'^{regex}$', input))


def _is_snake_case(
    input: str,
    disallow_digits: bool,
    separator_char: str,
    separator_allow_leading: bool,
) -> bool:
    regex = r''
    if disallow_digits is True:
        regex = r'[a-z]+(?:_[a-z]+)*'
        if separator_char:
            regex = (
                rf'[a-z]+(?:_[a-z]+)*(?:{separator_char}?[a-z]+(?:_[a-z]+)*)*'
            )
            if separator_allow_leading is True:
                regex = (
                    rf'{separator_char}?[a-z]+(?:_[a-z]+)*'
                    rf'(?:{separator_char}?[a-z]+(?:_[a-z]+)*)*'
                )
    else:
        regex = r'[a-z]+(?:_[a-z0-9]+)*'
        if separator_char:
            regex = (
                rf'[a-z]+(?:_[a-z0-9]+)*'
                rf'(?:{separator_char}?[a-z]+(?:_[a-z0-9]+)*)*'
            )
            if separator_allow_leading is True:
                regex = (
                    rf'{separator_char}?[a-z]+(?:_[a-z0-9]+)*'
                    rf'(?:{separator_char}?[a-z]+(?:_[a-z0-9]+)*)*'
                )
    return bool(re.match(rf'^{regex}$', input))


def _is_macro_case(
    input: str,
    disallow_digits: bool,
    separator_char: str,
    separator_allow_leading: bool,
) -> bool:
    regex = r''
    if disallow_digits is True:
        regex = r'[A-Z]+(?:_[A-Z]+)*'
        if separator_char:
            regex = (
                rf'[A-Z]+(?:_[A-Z]+)*(?:{separator_char}?[A-Z]+(?:_[A-Z]+)*)*'
            )
            if separator_allow_leading is True:
                regex = (
                    rf'{separator_char}?[A-Z]+(?:_[A-Z]+)*'
                    rf'(?:{separator_char}?[A-Z]+(?:_[A-Z]+)*)*'
                )
    else:
        regex = r'[A-Z]+(?:_[A-Z0-9]+)*'
        if separator_char:
            regex = (
                rf'[A-Z]+(?:_[A-Z0-9]+)*'
                rf'(?:{separator_char}?[A-Z]+(?:_[A-Z0-9]+)*)*'
            )
            if separator_allow_leading is True:
                regex = (
                    rf'{separator_char}?[A-Z]+(?:_[A-Z0-9]+)*'
                    rf'(?:{separator_char}?[A-Z]+(?:_[A-Z0-9]+)*)*'
                )
    return bool(re.match(rf'^{regex}$', input))


def casing(
    inputs: FunctionInputs
) -> List[str]:
    disallow_digits = inputs.options.disallow_digits
    separator_char = inputs.options.separator_char
    separator_allow_leading = inputs.options.separator_allow_leading
    casing_type = inputs.options.type
    casing_types = {
        'flat': _is_flat_case(
            inputs.target_value,
            disallow_digits,
            separator_char,
            separator_allow_leading,
        ),
        'camel': _is_camel_case(
            inputs.target_value,
            disallow_digits,
            separator_char,
            separator_allow_leading,
        ),
        'pascal': _is_pascal_case(
            inputs.target_value,
            disallow_digits,
            separator_char,
            separator_allow_leading,
        ),
        'kebab': _is_kebab_case(
            inputs.target_value,
            disallow_digits,
            separator_char,
            separator_allow_leading,
        ),
        'cobol': _is_cobol_case(
            inputs.target_value,
            disallow_digits,
            separator_char,
            separator_allow_leading,
        ),
        'snake': _is_snake_case(
            inputs.target_value,
            disallow_digits,
            separator_char,
            separator_allow_leading,
        ),
        'macro': _is_macro_case(
            inputs.target_value,
            disallow_digits,
            separator_char,
            separator_allow_leading,
        ),
    }
    if casing_types.get(casing_type) is False:
        return [f'{inputs.context} must be {casing_type} case.']
    return []
