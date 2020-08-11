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
    i = 0
    minimum = 1

    while minimum < n:
        if n % minimum == 0:
            i += 2
            minimum *= 2
        else:
            i += 1
            minimum += minimum

    return i
