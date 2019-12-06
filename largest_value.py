#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on: December 2019
# This program uses an array 
# to print out largest value in a random list

import random


def maximum_number(list_of_numbers):
    # this function print largest value in the list(array)

    max_number = list_of_numbers[0]

    for counter in range(0, len(list_of_numbers)):
        if list_of_numbers[counter] > max_number:
            max_number = list_of_numbers[counter]

    return max_number


def main():
    # this function uses a list(array)

    random_numbers = []
    max_value = 0

    print("The numbers are: ")
    for loop_counter in range(0, 9):
        a_single_number = random.randint(0, 10)
        random_numbers.append(a_single_number)
        print("{0}, ".format(a_single_number), end="")
    print("")

    max_value = maximum_number(random_numbers)

    print("")
    print("The largest value in the list is: {0} ".format(max_value))


if __name__ == "__main__":
    main()
