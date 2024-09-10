"""Practice with conditionals"""


def less_than_10(num: int) -> None:
    """Tell me if num mis < 10."""
    if num < 10:
        print("Small Number!")
    else:
        print("Big Number!")
    print("Have a nice day!")


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger."""
    if hungry:  # conditional / boolean expression
        print("eat some food silly goose!")  # "then" block
    else:
        print("Do your Comp 110 homework instead")  # "else" block
    print("I'm proud of you <3")  # either way, be kind to yourself


def check_first_letter(word: str, letter: str) -> str:
    """Check if letter is first character of word."""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="s"))
