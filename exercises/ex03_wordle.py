"""EX03 - Wordle The Game"""

__author__ = "730810493"


def main(secret: str) -> None:  # Takes the secret word as the input to the function.
    """The entrypoint of the program and main game loop."""
    number_of_turns: int = 7
    # Variable that stores the number of turns in the game (desired turns + 1 is needed since the turns variable begins at 1)
    turns: int = (
        1  # Counts the number of turns taken and is used as an index for the while loop.
    )
    win: bool = (
        False  # Sets the win condition to false and is only updated if the game is won.
    )
    while (
        turns < number_of_turns and not win
    ):  # To enter the while loop the user must have turns left and must not have won.
        print(f"=== Turn {turns}/6 ===")  # Prints the turn number the user is on.
        guess: str = input_guess(
            len(secret)
        )  # Calls input_guess and saves the users guess as guess.
        print(
            emojified(guess, secret)
        )  # Calls emojified and prints the return value to display the colored boxes.
        if (
            guess == secret
        ):  # If the guess is equal to the secret word, then the game is won and the loop is exited.
            win = True
            print(f"You won in {turns}/6 turns!")
            return None
        turns += 1  # Updates the turn variable to track the number of turns that have been taken.
    if not win:  # If the game is not won a consolation message is produced.
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    # Takes the length of the secret word and returns the guessed word.
    """Verifies the length of the user input"""
    user_input: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # Prompts the user for a word and stores it as user_input.
    while secret_word_len != len(
        user_input
    ):  # Checks if the user input is equal to the length of the secret word.
        user_input = input(f"That wasn't {secret_word_len} chars! Try again: ")
        # Prompts the user for another input word and updates the user_input variable with the new word.
    return user_input  # Returns the users guess.


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks the secret_word arguement for instances of the char_guess character"""
    assert len(char_guess) == 1  # Checks that char_guess is one character.
    index: int = 0  # Index to prevent infinite loop of while function.
    char_found: bool = (
        False  # Local variable that stores the bool function if the character is found.
    )
    while index < len(secret_word):
        # If the letter is found in the word, the char_found variable's value is updated to True.
        if secret_word[index] == char_guess:
            char_found = True
        index += 1  # Updates the index value to prevent infinite loop.
    return char_found  # Returns the variable storing the bool value (True if char_guess if found, False otherwise).


# Named Constants for the color of the guess boxes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Checks the guess against the secret word to reveal matches"""
    assert len(guess) == len(
        secret
    )  # Assertion to ensure the guess and secret inputs are the same length.
    index: int = (
        0  # Index that tracks the secret character the program is currently on.
    )
    index2: int = (
        0  # Index that tracks the guess character the program is currently on.
    )
    block_string: str = (
        ""  # Empty str that will store the color blocks accoriding to the matches.
    )
    while index < len(secret):
        char: str = secret[index]  # Stores the values of secret at the current index.
        if char == guess[index2]:
            # If the value of char (see line above for description) matches guess on the current index then a green box is added to block_string
            block_string += GREEN_BOX
        elif contains_char(
            secret, guess[index2]
        ):  # Calls the contains_char function using the secret input and the current index of guess.
            # If the character is found in the secret word by contains_char then a yellow box is added to block_string.
            block_string += YELLOW_BOX
        else:  # If the character of guess[index2] does not equal the variable char or is not found in the secret word by contains_char, a white box is added to block_string.
            block_string += WHITE_BOX
        index2 += 1  # Updates the index of the guess value.
        index += 1  # Updates the index of the secret value.
    return block_string  # Returns block_string with the values added by the while loop.


if __name__ == "__main__":
    # Allows the code to be ran as a module and makes it possible for the functions to be imported.
    main(secret="codes")
