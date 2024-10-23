"""Lesson in Class"""


def get_first(input: list[str]) -> str:
    """Returns the first element"""
    if len(input) == 0:  # if empty input
        return ""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Removes the first element of the list"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Removes AND Returns First Element"""
    first_element: str = input[0]
    input.pop(0)
    return first_element
