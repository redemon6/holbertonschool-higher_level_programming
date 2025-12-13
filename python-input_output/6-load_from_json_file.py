#!/usr/bin/python3
"""
Module 6-load_from_json_file
Defines a function to create a Python object from the JSON content of a file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object (Python data structure) from the content of a JSON file.

    The file is opened in read mode ('r') and UTF-8 encoding.
    This function uses json.load() to read the JSON stream and deserialize it
    into a Python object.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        any: The Python object created from the JSON file content.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
