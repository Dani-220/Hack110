"""Reference for Creating Lists"""

# Create an empty list
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor
# print(my_numbers)

# String Analogy
# my_name: str = "" # literal
# my_name: str = str() # constructor

# Adding a value to a list
my_numbers.append(1.5)
my_numbers.append(2.3)
# print(my_numbers)

# Creating an already populated lists
game_points: list[int] = [102, 86, 94]
print(game_points)

# Subscription Notation/Indexing
# print(game_points[2])
last_game: int = game_points[2]
# print(last_game)

# Modifying by Index
# (Because lists are mutable)
game_points[1] = 72
print(game_points)

# Getting the length
len(game_points)

# Removing an items
game_points.pop(1)
print(game_points)

# Function name: display
# Parameter: list of integers
# RV: None
# Print every element in the input list
# Call display on game_points


def display(game: list[int]) -> None:
    "Displays all elements of game"
    index: int = 0
    while index < len(game):
        print(game[index])
        index += 1


display(game_points)
