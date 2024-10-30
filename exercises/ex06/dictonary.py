"""Exercise 06 - Dictionary Utility Functions"""

__author__ = "730810493"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the key and value of a dictionary."""
    output: dict[str, str] = (
        {}
    )  # Creates a new dictonary that the invert key and values can be placed in.
    values: list[str] = (
        []
    )  # Creates a new list that can store the new key values and looped over to prevent duplicate keys.
    for key in input:
        if (
            input[key] in values
        ):  # If the new key value is found in the existing list of key values then an error message is presented.
            raise KeyError()  # Raises a KeyError.
        values.append(input[key])  # Adds the new key value to the values list.
        output[input[key]] = key  # Inverts the original key and values of input
    return output  # Returns the new dictonary with the keys and values duplicated.


def favorite_color(input: dict[str, str]) -> str:
    """Returns the most popular color"""
    count_values: dict[str, int] = (
        {}
    )  # Creates a dictonary that will store the color and its count.
    for key in input:
        if (
            input[key] in count_values
        ):  # If the value is found count_values then 1 is added to the value of key.
            count_values[input[key]] += 1  # Adds one to the value
        else:
            count_values[input[key]] = (
                1  # If the value is not found, a dictonary entry is created with a initia; value of 1
            )
    highest_count: int = (
        0  # Stores the highest value found in the count_values dictonary
    )
    color: str = ""  # Stores the name of the color with the highest count
    for key in count_values:
        if (
            count_values[key] > highest_count
        ):  # If the value of the entry is greater than the highest_count, then color is updated to that color.
            color = key
    return color  # Returns color, which is the color with the highest number of apperences.


def count(input: list[str]) -> dict[str, int]:
    """Returns a dictonary with each key being a unique value from the input and the value being the number of apperances of the key"""
    counter: dict[str, int] = (
        {}
    )  # Creates a dictonary for the unique values and their counts to be stored.
    for elem in input:  # Loops through every element in the input list.
        if (
            elem in counter
        ):  # If the element in the list is found in counter, the value of the counter is increased by one.
            counter[elem] += 1
        else:  # If the element is not found in the dictonary, the entry is added to the dictonary with a value of 1.
            counter[elem] = 1
    return counter  # Returns the dictonary created from the list.


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary with words grouped by their starting letter."""
    alphabetizer_storage: dict[str, list[str]] = (
        {}
    )  # Creates a dictonary that will store the letters and corrosponding words.
    for word in input:  # Loops over the list.
        first_letter: str = word[
            0
        ].lower()  # Creates a variable that stores the first letter of the word in lower case.
        if (
            first_letter in alphabetizer_storage
        ):  # If the letter is in the dictonary, then the word is appended to the list in the value of the dict.
            alphabetizer_storage[first_letter].append(word)
        else:  # If the letter is not in the dictonary, the letter is added as a key and the word is added as the value.
            alphabetizer_storage[first_letter] = [word]
    return alphabetizer_storage  # Returns the dict created with unique letters as arguements and a list of the words that have that first letter.


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    """Updates the attendance list with new information."""
    if (
        day in input
    ):  # If the day is in the dictonary, then the students are appended to the list in the value portion of the dictonary.
        input[day].append(student)
    else:  # If the day is not in the dictionary, the day is added as a key and the student is added as the value.
        input[day] = [student]
    return None
