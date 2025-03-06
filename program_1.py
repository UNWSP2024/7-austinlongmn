# Programmer: Austin Long
# Date: 2025-03-06
# Program: Rainfall

# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12
# months into a list. The program should calculate and display the total
# rainfall for the year, the average monthly rainfall, and the months with the
# highest and lowest amounts.

from typing import Any, Generator

# Declare months
MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


# Gets rainfall for a certain month from user
def get_rainfall(month: str) -> float:
    try:
        return float(input(f"Enter the amount of rainfall for {month} in inches: "))
    except ValueError:
        print("You must enter a valid number with no units")
        return get_rainfall(month)


# utility function to get the keys from a list of pairs
def get_keys(pairs: list[tuple[str, float]]) -> Generator[str]:
    return (key for key, _ in pairs)


def get_values(pairs: list[tuple[str, float]]) -> Generator[float]:
    return (value for _, value in pairs)


# Displays table with justification
def display_table(ordered_pairs: list[tuple[str, Any]]):
    max_key_len = max((len(key) for key in get_keys(ordered_pairs)))
    max_value_len = max((len(str(value)) for value in get_values(ordered_pairs)))

    for key, value in ordered_pairs:
        print(f"{key.ljust(max_key_len)} {str(value).rjust(max_value_len)}")


# Main program
def main():
    # Get month and rainfall for each month
    rainfall = [(month, get_rainfall(month)) for month in MONTHS]

    # Sum up all values in pairs
    total = sum(get_values(rainfall))

    # Get average rainfall
    average = total / len(rainfall)

    # Get min and max pairs by comparing their values
    min_rain = min(rainfall, key=lambda pair: pair[1])
    max_rain = max(rainfall, key=lambda pair: pair[1])

    # Call display_table function with results
    display_table(
        [
            ("Total rain", f"{total} in"),
            ("Average rain", f"{average} in"),
            ("Least rain", f"{min_rain[0]} ({min_rain[1]} in)"),
            ("Most rain",  f"{max_rain[0]} ({max_rain[1]} in)"),
        ]
    )


# Run program
if __name__ == "__main__":
    main()
