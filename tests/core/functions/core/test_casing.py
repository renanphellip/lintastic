import pytest
from lintastic.core.functions.core.casing import (
    _is_flat_case,
    _is_camel_case,
    _is_pascal_case,
    _is_kebab_case,
    _is_cobol_case,
    _is_snake_case,
    _is_macro_case,
)

@pytest.mark.parametrize(
    "input, disallow_digits, separator_char, separator_allow_leading, expected",
    [
        # Cenários sem dígitos permitidos e sem separadores
        ## Cenários válidos
        ("flatcase", True, '', False, True),
        ## Cenários inválidos
        ("flatcase123", True, '', False, False),
        ("flat123case", True, '', False, False),

        # Cenários com dígitos permitidos e sem separadores
        ## Cenários válidos
        ("flatcase", False, '', False, True),
        ("flatcase123", False, '', False, True),
        ("flat123case", False, '', False, True),
        ## Cenários inválidos
        ("123flatcase", False, '', False, False),

        # Cenários sem dígitos permitidos e com separadores
        ## Cenários válidos
        ("flatcase", True, ',', False, True),
        ("flatcase,flatcase", True, ",", False, True),
        ("flatcase,flatcase,flatcase", True, ",", False, True),
        ## Cenários inválidos
        ("flatcase,", True, ",", False, False),
        ("flatcase,flatcase,", True, ",", False, False),
        ("flatcase,flatcase,flatcase,", True, ",", False, False),
        ("flatcase,123", True, ",", False, False),
        ("flatcase,flatcase,123", True, ",", False, False),
        ("flatcase,flatcase,flatcase,123", True, ",", False, False),

        # Cenários com dígitos permitidos e com separadores
        ## Cenários válidos
        ("flatcase,flatcase123", False, ",", False, True),
        ("flatcase,flatcase,flatcase123", False, ",", False, True),
        ("flatcase123,flatcase123", False, ",", False, True),
        ("flatcase123,flatcase123,flatcase123", False, ",", False, True),
        ("flatcase,flat123case", False, ",", False, True),
        ("flatcase,flatcase,flat123case", False, ",", False, True),
        ("flat123case,flat123case", False, ",", False, True),
        ("flat123case,flat123case,flat123case", False, ",", False, True),
        ## Cenários inválidos
        ("flatcase,123", False, ",", False, False),
        ("flatcase,flatcase,123", False, ",", False, False),
        ("flatcase,flatcase,flatcase,123", False, ",", False, False),
    
        # Cenários sem dígitos permitidos e com separadores permitidos no início
        ## Cenários válidos
        (",flatcase", True, ",", True, True),
        (",flatcase,flatcase", True, ",", True, True),
        (",flatcase,flatcase,flatcase", True, ",", True, True),
        ## Cenários inválidos
        (",flatcase,", True, ",", True, False),
        (",flatcase,flatcase,", True, ",", True, False),
        (",flatcase,flatcase,flatcase,", True, ",", True, False),
        (",flatcase,123", True, ",", True, False),
        (",flatcase,flatcase,123", True, ",", True, False),
        (",flatcase,flatcase,flatcase,123", True, ",", True, False),

        # Cenários com dígitos permitidos e com separadores permitidos no início
        ## Cenários válidos
        (",flatcase123", False, ",", True, True),
        (",flatcase,flatcase123", False, ",", True, True),
        (",flatcase,flatcase,flatcase123", False, ",", True, True),
        (",flatcase123,flatcase123", False, ",", True, True),
        (",flatcase123,flatcase123,flatcase123", False, ",", True, True),
        (",flatcase,flat123case", False, ",", True, True),
        (",flatcase,flatcase,flat123case", False, ",", True, True),
        (",flat123case,flat123case", False, ",", True, True),
        (",flat123case,flat123case,flat123case", False, ",", True, True),
        ## Cenários inválidos
        (",123flatcase", False, ",", True, False),
        (",flatcase,123flatcase", False, ",", True, False),
        (",flatcase,flatcase,123flatcase", False, ",", True, False),
        (",flatcase,123", False, ",", True, False),
        (",flatcase,flatcase,123", False, ",", True, False),
        (",flatcase,flatcase,flatcase,123", False, ",", True, False),
    ],
)
def test_is_flat_case(input, disallow_digits, separator_char, separator_allow_leading, expected):
    assert _is_flat_case(input, disallow_digits, separator_char, separator_allow_leading) == expected


@pytest.mark.parametrize(
    "input, disallow_digits, separator_char, separator_allow_leading, expected",
    [
        ("camelCase", True, '', False, True),
        ("camelCase123", False, '', False, True),
        ("camel-case", True, "-", False, False),
        ("camelCaseMore", True, '', False, True),
        ("CamelCase", True, '', False, False),
    ],
)
def test_is_camel_case(input, disallow_digits, separator_char, separator_allow_leading, expected):
    assert _is_camel_case(input, disallow_digits, separator_char, separator_allow_leading) == expected


@pytest.mark.parametrize(
    "input, disallow_digits, separator_char, separator_allow_leading, expected",
    [
        ("PascalCase", True, '', False, True),
        ("PascalCase123", False, '', False, True),
        ("Pascal-case", True, "-", False, False),
        ("pascalCase", True, '', False, False),
        ("PascalCaseMore", True, '', False, True),
    ],
)
def test_is_pascal_case(input, disallow_digits, separator_char, separator_allow_leading, expected):
    assert _is_pascal_case(input, disallow_digits, separator_char, separator_allow_leading) == expected


@pytest.mark.parametrize(
    "input, disallow_digits, separator_char, separator_allow_leading, expected",
    [
        ("kebab-case", True, '', False, True),
        ("kebab-case-123", False, '', False, True),
        ("kebab_case", True, "_", False, False),
        ("kebabCase", True, '', False, False),
        ("-kebab-case", True, "-", True, True),
    ],
)
def test_is_kebab_case(input, disallow_digits, separator_char, separator_allow_leading, expected):
    assert _is_kebab_case(input, disallow_digits, separator_char, separator_allow_leading) == expected


@pytest.mark.parametrize(
    "input, disallow_digits, separator_char, separator_allow_leading, expected",
    [
        ("COBOL-CASE", True, '', False, True),
        ("COBOL-CASE-123", False, '', False, True),
        ("COBOL_CASE", True, "_", False, False),
        ("cobol-case", True, '', False, False),
        ("-COBOL-CASE", True, "-", True, True),
    ],
)
def test_is_cobol_case(input, disallow_digits, separator_char, separator_allow_leading, expected):
    assert _is_cobol_case(input, disallow_digits, separator_char, separator_allow_leading) == expected


@pytest.mark.parametrize(
    "input, disallow_digits, separator_char, separator_allow_leading, expected",
    [
        ("snake_case", True, '', False, True),
        ("snake_case_123", False, '', False, True),
        ("snake-case", True, "-", False, False),
        ("Snake_Case", True, '', False, False),
        ("_snake_case", True, "_", True, True),
    ],
)
def test_is_snake_case(input, disallow_digits, separator_char, separator_allow_leading, expected):
    assert _is_snake_case(input, disallow_digits, separator_char, separator_allow_leading) == expected


@pytest.mark.parametrize(
    "input, disallow_digits, separator_char, separator_allow_leading, expected",
    [
        ("MACRO_CASE", True, '', False, True),
        ("MACRO_CASE_123", False, '', False, True),
        ("MACRO-CASE", True, "-", False, False),
        ("Macro_Case", True, '', False, False),
        ("_MACRO_CASE", True, "_", True, True),
    ],
)
def test_is_macro_case(input, disallow_digits, separator_char, separator_allow_leading, expected):
    assert _is_macro_case(input, disallow_digits, separator_char, separator_allow_leading) == expected
