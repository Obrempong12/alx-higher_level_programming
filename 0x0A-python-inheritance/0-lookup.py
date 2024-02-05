#!/usr/bin/python3
"""Defines an object attribute lookup func"""


def lookup(obj):
    """Return a list of an object's available attributes"""
    return (dir(obj))
