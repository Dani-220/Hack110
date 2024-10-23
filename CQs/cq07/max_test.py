"""In class challenge question"""

__author__ = "730810493"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    """find_and_remove_max should return the max element"""
    high_scores: list[int] = [
        95,
        100,
        200,
        4,
        200,
        10,
        200,
    ]  # high_scores is the list being used to test the function.
    assert (
        find_and_remove_max(high_scores) == 200
    )  # tests if the function returns the desired max value.


def test_find_and_remove_max_mutation() -> None:
    """find_and_remove_max should remove all instances of the max element"""
    high_scores: list[int] = [
        95,
        100,
        200,
        4,
        200,
        10,
        200,
    ]  # high_scores is the list being used to test the function.
    find_and_remove_max(
        high_scores
    )  # Calls the function so that it mutates the input list.
    assert high_scores == [
        95,
        100,
        4,
        10,
    ]  # tests if the function correclty mutated the list.


def test_find_and_remove_max_edge_case() -> None:
    """find_and_remove_max should return -1 when an empty list is inputed"""
    assert (
        find_and_remove_max([]) == -1
    )  # tests if the function returns -1 when an empty list is inputed.
