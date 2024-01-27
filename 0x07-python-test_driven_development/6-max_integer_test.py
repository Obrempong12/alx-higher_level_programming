#!/usr/bin/python3
"""Module to find the maximum int in a list.
"""


def max_integer(list=[]):
    """Func to find and return the maximum int in a list of integers.
        If the list is empty, the function returns None.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
