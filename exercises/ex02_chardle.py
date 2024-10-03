"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730810493"


def main() -> None:
    "Entry point for the chardle game"
    contains_char(
        word=input_word(), letter=input_letter()
    )  # Calls the contains_char function with the input_word and input_letter functions as arguements.


def input_word() -> str:
    """Verify the length of word input"""
    promt: str = input(
        "Enter a 5-character word: "
    )  # Saves the input from the user as promt.
    if (
        len(promt) == 5
    ):  # Checks if promt is 5 characters and returns promt if it meets criteria.
        return promt
    else:
        print("Error: Word must contain 5 characters.")
        exit()  # Exits the program is the user has an invalid input for word.
        return promt  # If promt is less than 5 characters the else statement notifies the user and returns prompt.


def input_letter() -> str:
    """Verify the length of the letter input"""
    character: str = input(
        "Enter a single character: "
    )  # Saves the character input from the user as character.
    if (
        len(character) == 1
    ):  # Checks if the character in the variable character length = 1
        return character  # If the variables length is one character the character is returned.
    else:
        print("Error: Character must be a single character.")
        exit()  # Exits the program is the user has an invalid input for letter.
        return character  # If the characters length is not 1 then an error message is printed and the character is returned.


def contains_char(word: str, letter: str) -> None:
    "Checks the input word for matches of the input letter"
    count: int = (
        0  # Variable that stores the number of instances of the character found.
    )
    print(
        "Searching for " + letter + " in " + word
    )  # Notifies the user that the program is searching for matches in the word.
    if (
        letter == word[0]
    ):  # Searches each index of the letter and prints a string if the letter is found at the index. Also adds one to the variable count if a match is found.
        print(letter + " found at index 0")
        count += 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count += 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count += 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count += 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count += 1
    if (
        count == 0
    ):  # If no instances of the letter is found a string is printed notifying the user.
        print("No instances of " + letter + " found in " + word)

    else:  # If instances of the letter is found the user is notified with one the strings below.
        if count == 1:  # Notifies with this string if 1 match is found.
            print(str(count) + " instance of " + letter + " found in " + word)
        else:  # Notifies with this string if more than one match is found.
            print(str(count) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
# Necessary for the code to run.
