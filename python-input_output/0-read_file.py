#!/usr/bin/python3
"""
Module 0-read_file
Defines a function to read a text file and print its contents to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8 encoding) and prints its content to stdout.

    Uses the 'with' statement to ensure the file is properly closed after
    reading.

    Args:
        filename (str): The name of the file to read. Defaults to an empty
        string.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
