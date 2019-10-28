#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: October 2019
# This is a program which tells you the total value of a number.


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def main():
    # This is what runs the program.
    print("")
    print("This program will tell you the"
          " numbers which square into another number...")
    print('')

    while True:
        # Input
        number_as_string = input(color.BOLD + color.YELLOW + 'Input a positive'
                                 ' and whole number: ' + color.END)
        number_total = 0
        next_full_number = 0

        # This is the joe mama easter egg, its just for fun.
        if number_as_string == ("who's joe"):
            print("")
            print(color.BOLD + 'JOE MAMA!' + color.END)
            print(color.RED + 'Joe mama mode has now been enabled...'
                  + color.END)

        # Process
        try:
            chosen_number = int(number_as_string)

            if chosen_number > 0:
                for next_full_number in range(chosen_number + 1):
                    print("{0}^2 = {1}" .format(next_full_number,
                                                next_full_number**2))
                    number_total = number_total + next_full_number**2

                print(color.GREEN + 'total = {0}'.format(number_total)
                      + color.END)
                break

            else:
                print('')
                print(color.PURPLE + color.UNDERLINE + 'That is not a positive'
                      ' and/or whole number...' + color.END)
                print("")
                print("")

        # This stops them from putting in something let bob and gets them to
        # re-input their age.
        except Exception:
            print('')
            print(color.PURPLE + color.UNDERLINE + 'That is not a positive'
                  ' and/or whole number...' + color.END)
            print("")
            print("")


if __name__ == "__main__":
    main()
