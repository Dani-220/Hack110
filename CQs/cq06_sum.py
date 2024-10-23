"""Summing the elements of a list using different loops"""

__author__ = "730810493"


def w_sum(val: list[float]) -> float:
    """Calculates the sum of a list"""
    if len(val) == 0:  # Returns the value of 0 if the list is empty.
        return 0.0
    index: int = 0  # Index used for tracking the while loop.
    total: float = (
        0  # Variable that tracks the total value of the elements in the list.
    )
    while index < len(val):
        total += val[
            index
        ]  # Adds the element of the list at index to the total varaible.
        index += 1  # Updates the value of index.
    return total  # Returns the total variable, which stores the total value of all elements in the list.


def f_sum(val: list[float]) -> float:
    """Calculates the sum of the input list"""
    total: float = (
        0  # Variable that tracks the total value of the elements in the list.
    )
    for elem in val:
        total += elem  # Adds the elem to the total of the elements in the list.
    return total  # Returns the total variable with the value of all the elements in the list.


def f_range_sum(val: list[float]) -> float:
    """Calculates the sum of the input list"""
    total: float = (
        0  # Variable that tracks the total value of the elements in the list.
    )
    for index in range(0, len(val)):
        total += val[index]  # Adds the elem to the total of the elements in the list.
    return total  # Returns the total variable with the value of all the elements in the list.
