"""A simple number guessing game!"""

__author__ = "730810493"


def guess_a_number() -> None:
    # Creates a guessing game based on secret number and guess
    secret: int = 7
    x: int = int(input("Guess a number: "))
    print("Your guess was " + str(x))
    if x == secret:
        print("You got it!")
    elif secret > x:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
