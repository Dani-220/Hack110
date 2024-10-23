"""In class challenge question"""

__author__ = "730810493"


def find_and_remove_max(input: list[int]) -> int:
    """Returns the largest number and removes all instances of that number"""
    if (
        len(input) == 0
    ):  # Checks if an empty list was inputed and returns -1 if there was an empty list inputted.
        return -1
    high_value: int = (
        0  # Sets the value of the variable that will hold the max value to 0.
    )
    for (
        elem
    ) in (
        input
    ):  # for look that compares each element in the list to find the max value.
        if elem >= high_value:
            high_value = elem  # stores the max value in high_value
    index: int = 0  # index used for tracking the while loop
    while index < len(input):
        if (
            input[index] == high_value
        ):  # if the input at index matchs the high_value it is removed from the list
            input.pop(index)
            index -= 1
        index += 1  # updates the value of the index
    return high_value  # returns the max value of the list prior to mutation.
