#!/usr/bin/python3
"""
Module 2-is_same_class
Defines a function to check for exact class instance matching.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    This function uses the built-in type() function to ensure that
    the object's class is not a subclass of a_class, but precisely a_class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    if type(obj) is a_class:
        return True
    return False
