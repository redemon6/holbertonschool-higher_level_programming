#!/usr/bin/python3
"""
Module 0-lookup
Defines a function that retrieves and returns the list of attributes
and methods associated with an object.
"""


def lookup(obj):
    """
    Returns a list of an object's available attributes and methods.

    This function uses the built-in dir() function to perform object
    introspection, listing all valid attributes of the given object.

    Args:
        obj: The object (instance or class) to inspect.

    Returns:
        list: A list containing the names of attributes and methods.
    """
    return dir(obj)
