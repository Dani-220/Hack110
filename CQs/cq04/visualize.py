"""Visualize"""

__author__ = "730810493"

from CQs.cq04.concatenation import (
    concat,
)  # imports the concat function from concatenation

x: str = "123"  # creates global var that stores the value "123"
y: str = "abc"  # creates globel var that stores the value "abc"

print(concat(x, y))  # prints the concat function with the global vars x and y

from CQs.cq04.coordinates import (
    get_coords,
)  # imports the get_coords function from coordinates

get_coords(x, y)  # calls the get_coords function with the global variables x, y
