"""Concatenation"""

__author__ = "730810493"


def concat(str_one: str, str_two: str) -> str:
    "Concatenates two strings together"
    return str_one + str_two  # concatenates the two strings together


word1: str = "happy"  # global var that stores the value happy
word2: str = "tuesday"  # global var that stores the value tuesday

if __name__ == "__main__":  # prevents the visualize file from printing when importing
    print(concat(word1, word2))
