from typing import Any
import pytest
from lintastic.core.functions.core.alphabetical import alphabetical
from lintastic.core.entities.functions.alphabetical import AlphabeticalFunctionInputs, AlphabeticalFunctionOptions

@pytest.fixture
def mock_inputs():
    def _create_inputs(target_value: Any, keyed_by='') -> AlphabeticalFunctionInputs:
        return AlphabeticalFunctionInputs(
            rule_name='test_rule',
            context='$',
            field='tags',
            options=AlphabeticalFunctionOptions(keyed_by=keyed_by),
            target_value=target_value,
        )
    return _create_inputs


def test_alphabetical_dict_unsorted(mock_inputs):
    inputs = mock_inputs(target_value={'tags': {'b': 1, 'a': 2}})
    result = alphabetical(inputs)
    assert result == ['"$.tags" object should have alphabetical keys.']


def test_alphabetical_dict_sorted(mock_inputs):
    inputs = mock_inputs(target_value={'tags': {'a': 1, 'b': 2}})
    result = alphabetical(inputs)
    assert result == []


def test_alphabetical_list_unsorted(mock_inputs):
    inputs = mock_inputs(target_value={'tags': ['beta', 'alpha', 'gamma']})
    result = alphabetical(inputs)
    assert result == ['"$.tags" list should have alphabetical values.']


def test_alphabetical_list_sorted(mock_inputs):
    inputs = mock_inputs(target_value={'tags': ['alpha', 'beta', 'gamma']})
    result = alphabetical(inputs)
    assert result == []


def test_alphabetical_list_unsorted_keyed_by(mock_inputs):
    inputs = mock_inputs(
        target_value={'tags': [{'name': 'beta'}, {'name': 'alpha'}, {'name': 'gamma'}]},
        keyed_by='name'
    )
    result = alphabetical(inputs)
    assert result == ['"$.tags" list should have alphabetical objects sorted by "name".']


def test_alphabetical_list_sorted_keyed_by(mock_inputs):
    inputs = mock_inputs(
        target_value={'tags': [{'name': 'alpha'}, {'name': 'beta'}, {'name': 'gamma'}]},
        keyed_by='name'
    )
    result = alphabetical(inputs)
    assert result == []


def test_alphabetical_list_keyed_by_missing_key(mock_inputs):
    inputs = mock_inputs(
        target_value={'tags': [{'name': 'alpha'}, {'other_key': 'beta'}]},
        keyed_by='name'
    )
    result = alphabetical(inputs)
    assert result == []


def test_alphabetical_field_not_list_or_dict(mock_inputs):
    inputs = mock_inputs(target_value={'tags': 'not_a_list_or_dict'})
    result = alphabetical(inputs)
    assert result == []


def test_alphabetical_empty_target_value(mock_inputs):
    inputs = mock_inputs(target_value={})
    result = alphabetical(inputs)
    assert result == []
