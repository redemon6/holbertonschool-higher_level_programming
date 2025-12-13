#!/usr/bin/python3
"""
Module 3-to_json_string
Defines a function to return the JSON string representation of an object.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Uses the 'json.dumps()' method for serialization.

    Args:
        my_obj (any): The Python object (e.g., list, dict) to serialize.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
