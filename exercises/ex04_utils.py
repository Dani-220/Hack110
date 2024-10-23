"""List Utility Functions Exercise"""

__author__ = "730810493"


def all(
    input_list: list[int], number: int
) -> bool:  # Takes a list and a number to satisfy its perameters.
    """Checks if all instances of a list are the number"""
    if (
        len(input_list) == 0
    ):  # If the length of the list is 0, the function returns False.
        return False
    index: int = 0  # Index variable for tracking the while loop.
    while index < len(input_list):
        if input_list[index] != number:
            # If the number does not equal the list value at index then the function is stopped and a value of false is returned.
            return False
        index += 1  # Updates the index variable.
    return True  # Returns true if the while loop is successfully completed.s


def max(input: list[int]) -> int:
    """Returns the max value in a list"""
    if len(input) == 0:  # If the list is empty a ValueError is raised.
        raise ValueError("max() arg is an empty List")
    index: int = 0  # Index variable for tracking the while loop.
    high_value: int = input[
        0
    ]  # Sets the max value to the first value in the list and stores the value as high_value.
    while index < len(input):
        if (
            input[index] >= high_value
        ):  # If the value of the list at index is greater than or equal to the high value the high value is updated.
            high_value = input[index]
        index += 1  # Updates the index variable.
    return high_value  # Returns the max value found in the list.


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if every element at every index is equal in both lists"""
    if len(list_1) != len(list_2):  # If the lists are not equal, False is returned.
        return False
    index: int = 0  # Index for tracking the while loop and the value list_1.
    index2: int = 0  # Index for tracking the while loop and the value for list_2
    while index < len(list_1) or index2 < len(list_2):
        # Enters the function if the index for either list is less than the number of elements in the list/
        if (
            list_1[index] != list_2[index2]
        ):  # If the elements in the list are not equal the function is exited and False is returned.
            return False
        index += 1  # Updates the index value.
        index2 += 1  # Updates the index2 value.
    return True  # Returns true if the while loop is successfully ran without returning False.


def extend(
    input1: list[int], input2: list[int]
) -> None:  # Accepts two list as arguements.
    """Appends list 2 (input2) to the end of list 1 (input1)"""
    index: int = 0  # Index used for tracking the while loop and position in input2.
    while index < len(input2):
        input1.append(
            input2[index]
        )  # Appends the element of input2 at index to the end of input1.
        index += 1  # Updates the index value.
    return None
