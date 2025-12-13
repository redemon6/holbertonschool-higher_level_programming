#!/usr/bin/python3
"""
Module 5-save_to_json_file
Defines a function to write a Python object to a file using its JSON repr.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using a JSON representation.

    The file is opened in write mode ('w') and UTF-8 encoding.
    This function uses json.dump() to serialize and write to the file stream
    in one step.

    Args:
        my_obj (any): The Python object to be serialized and saved.
        filename (str): The name of the file to write the JSON string to.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
