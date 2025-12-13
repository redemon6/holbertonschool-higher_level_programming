#!/usr/bin/python3
"""
Module 2-append_write
Defines a function to append a string to a text file and return the
number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns
    the number of characters added.

    The file is opened in append mode ('a'), which creates the file
    if it does not exist and places the writing cursor at the end
    of the file if it does.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string content to append to the file.

    Returns:
        int: The number of characters successfully added to the file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
