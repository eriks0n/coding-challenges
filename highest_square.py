#!/usr/bin/env python3

def highest_square_below(number):
    """ 
    Calculating and returning the highest square below a given number.

    Args:
        number: Given number which acts as the upper bound
    Returns:
        highest_square: The highest square which es less than the given number
    """

    highest_square = 0

    for i in range(1, number):

        square = i ** 2

        if square > number:
            break
        highest_square = square

    return highest_square



if __name__ == "__main__":
    print(highest_square_below(500))
