#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Defines a function to check for inherited class instance matching.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if it is an instance of
    a class that inherited from, the specified class.

    This function uses the built-in isinstance() function to check for
    inheritance along the object's Method Resolution Order (MRO).

    Args:
        obj (any): The object to check.
        a_class (type): The class (or parent class) to match against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass of a_class,
              False otherwise.
    """
    return isinstance(obj, a_class)
