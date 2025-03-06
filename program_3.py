# Programmer: Austin Long
# Date: 2025-03-06
# Program: US Population

from typing import Callable, Any
import sys, os

# Yeah... I got a little carried away with this one...


# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data:
    # year, name of state, and population.
    # Store all of this information in a list of lists.  For example it might be stored like this:

    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []

    # Now have the user enter a year.

    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

    # Get user input loop
    while True:
        done, values = input_entry()
        if done:
            break
        # Add value to accumulator
        all_entered_values.append(values)

    # calculate result
    sum_population_for_year(
        all_entered_values,
        get_input(
            "Enter the year to sum: ",
            int,
            "You must enter a valid year.",
            lambda x: x > 0,
        ),
    )


# Inputs a year, state, and population. Returns (True, None) if done or (False,
# value) if not.
def input_entry() -> tuple[bool, tuple[int, str, int] | None]:
    # check if the user is done on the first one.
    done, first_value = interactive_get_input(
        "Enter the year for the entry (blank to quit): ",
        int,
        "You must enter a valid year.",
        lambda x: x > 0,
    )

    if done:
        return True, None

    # if there are more values, return them.
    return (
        False,
        (
            first_value,
            get_input("Enter the state: ", str),
            get_input(
                "Enter the population: ",
                int,
                "You must enter a valid population.",
                lambda x: x > 0,
            ),
        ),
    )


# Gets input where the user is not expected to quit.
def get_input(
    prompt: str,
    conversion: Callable[[str], Any],
    err_message: str = "Invalid input.",
    validation: Callable[[Any], bool] = lambda _: True,
) -> Any:
    return interactive_get_input(prompt, conversion, err_message, validation, None)[1]


# Gets input. If the user inputs terminator, then the function signals this to the caller.
def interactive_get_input(
    prompt: str,
    conversion: Callable[[str], Any],
    err_message: str = "Invalid input.",
    validation: Callable[[Any], bool] = lambda _: True,
    terminator: str | None = "",
) -> tuple[bool, Any]:
    try:
        # Gets input from user. If the program isn't running in interactive
        # mode, this skips prompting.
        user_input = input(prompt if os.isatty(0) else "")

        # If terminator found, signal to caller.
        if terminator != None and user_input == terminator:
            return (True, None)

        # convert input
        converted = conversion(user_input)

        # Check input validity
        if validation(converted):
            # Return successful value
            return (False, converted)
    except ValueError:
        pass

    # Retry input if error
    print(err_message, file=sys.stderr)
    return get_input(prompt, conversion, err_message, validation)


def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year.
    # e.g. for the list on line 7 the total would be 8,860,637 if the user entered 2010 for the year to sum,
    # or 3,421,988 if they entered 2011 for the year to sum.

    # print the totalled population

    # Calculate grand total. Breakdown: The population for every entry whose
    # year is year_to_sum.
    grand_total = sum(
        [
            value[2]
            for value in filter(
                lambda value: value[0] == year_to_sum, all_entered_values
            )
        ]
    )

    # Display output.
    print(f"The total population for year {year_to_sum} is {grand_total}")


# Call the main function.
if __name__ == "__main__":
    main()
