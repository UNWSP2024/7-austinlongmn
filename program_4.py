# Programmer: Austin Long
# Date: 2025-03-06
# Program: Coordinates

# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input)
# and will return (as output) the distance between those points in space.
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)

import math
import re

# Please go to program_3.py to see my user input function.
from program_3 import get_input


# Finds the distance between the two points
def distance(point_a: tuple[float, float, float], point_b: tuple[float, float, float]):
    return math.sqrt(
        (point_b[0] - point_a[0]) ** 2
        + (point_b[1] - point_a[1]) ** 2
        + (point_b[2] - point_a[2]) ** 2
    )


# Converts a string in the form (x, y, z) to a Python tuple
def point_from_str(string_tuple: str) -> tuple[float, float, float]:
    # match regex against string
    regex_match = re.match(
        r"\s*\(\s*([0-9.]+)\s*,\s*([0-9.]+)\s*,\s*([0-9.]+)\s*\)\s*", string_tuple
    )
    if regex_match: # if regex matched, then convert strings into floats and return
        return (float(regex_match[1]), float(regex_match[2]), float(regex_match[3]))
    else: # else raise ValueError
        raise ValueError(f"String is not a valid point: {string_tuple}")


def main():
    # get user input
    err_message = "Error: you must enter a point in the form (x, y, z)"
    point_a = get_input("Enter point A: ", point_from_str, err_message)
    point_b = get_input("Enter point B: ", point_from_str, err_message)

    # diplay result
    print(distance(point_a, point_b))


# Run program
if __name__ == "__main__":
    main()
