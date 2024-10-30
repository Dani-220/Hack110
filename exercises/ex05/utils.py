"""EX05 - 'list' Utility Functions"""

__author__ = "730810493"


def only_evens(input: list[int]) -> list[int]:
    """Returns a list of the even elements in input"""
    output: list[int] = []  # Creates an empty list for elements to be stored in.
    for elem in input:  # Loops through all of the elements in input.
        if elem % 2 == 0:  # If the element is even it is appended to output.
            output.append(elem)
    return output  # Returns the list output.


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Returns a subset of the input list between the start and end index"""
    if (
        len(input) == 0 or start > len(input) or end <= 0
    ):  # If the user input is not within the specification of the function use case, [] is returned.
        return []
    if start < 0:  # Sets the start value to 0 if the user input is less than 0.
        start = 0
    if end > len(
        input
    ):  # Sets the end value to the end of the list if the user's end value is greater than the length of the list.
        end = len(input)
    output: list[int] = []  # Creates an empty list for elements to be stored in
    index: int = 0  # Index used for tracking the while loop.
    while index < len(input):
        if (
            index >= start and index < end
        ):  # If the index is within the start and end range then the element of the list is append to the output placeholder.
            output.append(input[index])
        index += 1  # Updates the index variable.
    return output  # Returns the output list that was filled with elements from the while loop.


def add_at_index(input: list[int], element: int, index: int) -> None:
    """Adds the element to the list at the desired index"""
    if index < 0 or index > len(
        input
    ):  # If the index is less than one or if it is greater than the length of the list, an IndexError is raised.
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)  # Adds a placeholder to the end of the list
    space: int = (
        len(input) - 1
    )  # Sets the space variable equal to the last value in the list.
    while space > index:  # While space is less than the index, the loop is ran.
        input[space] = input[
            space - 1
        ]  # Moves the number to the left of input[space] to input[space].
        space -= 1  # Updates the value of space to move one to the left.
    input[index] = (
        element  # Adds the value of the element after every variable has been moved over.
    )
    return None
