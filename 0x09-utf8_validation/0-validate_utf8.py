#!/usr/bin/python3
"""
determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    :param data: list of integers
    :return: True if data is a valid UTF-8 encoding, else return False
    """
    is_valid_utf8 = True
    for integer in data:
        if integer > 255:
            is_valid_utf8 = False

    return is_valid_utf8
