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
    try:
        if bytes(data):
            return True
    except ValueError:
        return False
