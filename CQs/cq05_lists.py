"""Mutating Functions"""

__author__ = "730810493"


def manual_append(
    input_list: list[int], number: int
) -> None:  # Takes a list and int as arguements to satisfy parameters.
    """Appends number to input_list"""
    input_list.append(number)  # Appends number to the end of input_lists.
    return None  # Return value is None


def double(
    need_list: list[int],
) -> None:  # Takes a list as the arguement to satisy parameters.
    """Doubles each value in the list"""
    index: int = 0  # Index for tracking the while loop.
    while index < len(need_list):  # Loops through each index of the list.
        need_list[index] *= 2  # Multiplies the value of the list by two at index.
        index += 1  # Updates the index value to track the loop.
    return None


list_1: list[int] = [1, 2, 3]  # Global variable for a list.
list_2: list[int] = list_1  # Global variable for a list that has the same id as list_1.

double(list_2)  # Calls the double function with list_2 as the arguement.
print(list_1)  # Prints list_1
print(list_2)  # Prints list_2
