"""Practice with scope"""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""  # Set up empty str to copy values over
    index: int = 0
    print(word)
    while index < len(msg):
        # if the letter is NOT char
        if not (msg[index] == char):  # if msg[index] != char
            copy += msg[index]  # copy = copy + msg[index]
        index += 1

    return copy


# create a variable called word with the value "yoyo"
word: str = "yoyo"  # GLOBAL variable
# print the result of calling you function with arguments word and "y"
print(remove_chars(word, "y"))
# print the result of calling you function with arguments word and "0"
print(remove_chars(word, "o"))  # with positional arguements
