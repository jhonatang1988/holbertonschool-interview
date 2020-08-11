#!/usr/bin/python3
"""
an algorithm to calculate minimumOperations necessary to get to a number of
characters.
Full exercise:
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.
"""


def minOperations(n):
    """
    minimumOperations
    :param n: number to reach calculating minimumOperations before get to it
    :return: an integer, which is the fewest number of operations needed to
    result in exactly n H characters in the file or 0 if n is impossible to
    achieve
    """
    if n <= 0:
        return 0
    if n == 1:
        return 0
    operations = 0
    characters = 1
    additive = 1

    while characters < n:
        if n % characters == 0:
            operations += 2
            additive = characters
            characters += additive
            # print('DIVISIBLE! operations: {}, characters: {}'
            #       .format(operations, characters))

        else:
            characters += additive
            operations += 1
            # print('NON! operations: {}, characters: {}'
            #       .format(operations, characters))

    return operations
