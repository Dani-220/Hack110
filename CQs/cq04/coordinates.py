"""Coordinates"""

__author__ = "730810493"


def get_coords(xs: str, ys: str) -> None:
    "Prints coordinate pairs"
    index: int = 0  # index variable for tracking while loop
    while index < len(xs):
        val: str = xs[index]  # stores the input value at the current index
        index2: int = (
            0  # index variable for tracking nested while loop (also allows the loop to be rentered)
        )

        while index2 < len(ys):  # while loop that loops over the ys variable
            val2: str = ys[index2]  # stores the input value at the current index for ys
            print(
                "(" + val + "," + val2 + ")"
            )  # Concadinates the two variables to correct format.
            index2 += 1  # adds one to index2 to prevent infinite loop
        index += 1  # adds one to index to prevent infinite loop
