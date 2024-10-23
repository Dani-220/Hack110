"""Testing utils.py"""

__author__ = "730810493"

from exercises.ex05.utils import (
    only_evens,
    sub,
    add_at_index,
)  # Imports the functions from utils.py
import pytest  # Imports pytest for the IndexError test


def test_only_evens_return_value() -> None:
    """Tests the return value of only_evens with regular use case"""
    numbers: list[int] = [
        97,
        32,
        26,
        44,
        95,
        103,
    ]  # Creates a list that can be used in the test
    assert only_evens(numbers) == [
        32,
        26,
        44,
    ]  # Asserts that only_evens returns the even values from the list numbers.


def test_only_evens_mutation() -> None:
    """Tests only_evens to see if the function mutations the list"""
    numbers: list[int] = [
        97,
        32,
        26,
        44,
        95,
        103,
    ]  # Creates a list that can be used in the test.
    only_evens(numbers)  # Calls only_evens with numbers as input.
    assert numbers == [
        97,
        32,
        26,
        44,
        95,
        103,
    ]  # Tests if numbers was mutated by the only_evans function call.


def test_only_evens_empty_list() -> None:
    """Tests only_evens with an empty list"""
    numbers: list[int] = []  # Creates an empty list that can be used in the test.
    assert (
        only_evens(numbers) == []
    )  # Tests if only_evens returns an empty list when given an empty list.


def test_sub_return_value() -> None:
    """Tests the return value of sub with regular use case"""
    numbers: list[int] = [
        97,
        32,
        26,
        44,
        95,
        103,
    ]  # Creates a list that can be used in the test
    assert sub(numbers, 2, 4) == [
        26,
        44,
        95,
    ]  # Tests if sub returns the correct subset.


def test_sub_mutation() -> None:
    """Tests if sub mutates the original list"""
    numbers: list[int] = [
        97,
        32,
        26,
        44,
        95,
        103,
    ]  # Creates a list that can be used in the test
    sub(numbers, 3, 5)  # Calls the sub function with numbers, 3, and 5 as arguements.
    assert numbers == [
        97,
        32,
        26,
        44,
        95,
        103,
    ]  # Tests if the sub function mutated the numbers list when called.


def test_sub_end_out_of_range() -> None:
    """Tests subs output when the end element is out of range of the list"""
    numbers: list[int] = [
        97,
        32,
        26,
        44,
        95,
        103,
    ]  # Creates a list that can be used in the test
    assert sub(numbers, 3, 10) == [
        44,
        95,
        103,
    ]  # Tests if sub correctly assesd the end of the range and provided the correct output.


def test_add_at_index_return_value() -> None:
    """Tests the return value of add_at_index with regular use case"""
    numbers: list[int] = [
        97,
        32,
        26,
        44,
        95,
        103,
    ]  # Creates a list that can be used in the test
    assert (
        add_at_index(numbers, 1, 2) == None
    )  # Tests if add_at_index returns a value of None.


def test_add_at_index_mutation() -> None:
    """Tests if add_at_index mutates the original list"""
    numbers: list[int] = [
        97,
        32,
        26,
        44,
        95,
        103,
    ]  # Creates a list that can be used in the test
    add_at_index(
        numbers, 1, 2
    )  # Calls add_at_index with the arguments numbers, 1, and 2.
    assert numbers == [
        97,
        32,
        1,
        26,
        44,
        95,
        103,
    ]  # Checks if 1 was added at the correct index.


def test_add_at_index_IndexError():
    """Test that add_at_index raises an IndexError for an out of range index."""
    with pytest.raises(IndexError):  # Uses pytest
        numbers: list[int] = [
            97,
            32,
            26,
            44,
            95,
            103,
        ]  # Creates a list that can be used in the test
        add_at_index(numbers, 1, 100)
        # Raises an IndexError for the case when the function is given an index that is greater than the length of the list.
