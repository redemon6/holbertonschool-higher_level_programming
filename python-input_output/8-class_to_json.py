#!/usr/bin/python3
"""
Defines a function that returns the dictionary description of an object
for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of an object containing only
    serializable simple data structures.

    Args:
        obj (object): An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary containing the object's attributes.
    """
    return obj.__dict__
