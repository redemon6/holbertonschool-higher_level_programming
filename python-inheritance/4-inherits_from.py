#!/usr/bin/python3
"""
Module 4-inherits_from
Defines a function to check for indirect inheritance from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    This means the object must be an instance of a SUBCLASS of a_class,
    and not an instance of a_class itself.

    Args:
    obj (any): The object to check.
        a_class(type): The class (or parent class) to match against.

    Returns:
      bool:True if the object's class is a subclass of a_class
              and the object's class is not a_class itself, False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
