#!/usr/bin/python3
"""
Module 1-write_file
Defines a function to write a string to a text file and return the
number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters
    written.
    The function opens the file in write mode ('w'), which creates the file
    if it doesn't exist or overwrites its content if it does.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string content to write to the file.

    Returns:
        int: The number of characters successfully written to the file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
