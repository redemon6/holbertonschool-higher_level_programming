#!/usr/bin/python3
"""
Module 10-square
Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance after validating size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

