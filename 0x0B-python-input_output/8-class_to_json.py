#!/usr/bin/python3
"""Defines a Python class-to-JSON func."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data struc."""
    return obj.__dict__
