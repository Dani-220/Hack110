"""While Loops Interating Over a String"""

__author__ = "730810493"


def num_instances(phrase: str, search_char: str) -> int:
    """Returns number of search character in string"""
    count: int = 0  # variable that counts the instances of the letter
    index: int = 0  # tracks the amount of while loops initated
    while index < len(phrase):  # loops through phrase looking for search_char
        if phrase[index] == search_char:
            count = count + 1
            index = index + 1
        else:
            index = index + 1
    return count  # returns the amount of search characters found in phrase
