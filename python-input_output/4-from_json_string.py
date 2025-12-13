#!/usr/bin/python3
"""
Module 4-from_json_string
Defines a function to return a Python object from a JSON string representation
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Uses the 'json.loads()' method for deserialization.

    Args:
        my_str (str): The JSON string representation of the object.

    Returns:
        any: The Python data structure (e.g., list, dict) represented by the
        string.
    """
    return json.loads(my_str)
