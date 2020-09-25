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
    if not data:
        return True
    eight_least = []
    try:
        for i in data:
            eight_least.append(i & 0xFF)
        bits = bytes(eight_least)
        bits.decode('utf-8')
        return True
    except ValueError:
        return False
