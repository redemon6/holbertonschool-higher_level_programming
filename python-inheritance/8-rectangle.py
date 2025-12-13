#!/usr/bin/python3
"""
Module 8-rectangle
Defines a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
and uses the inherited integer_validator for attribute validation.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting validation and structure
    from BaseGeometry.

    Attributes:
        __width (int): The private width of the rectangle.
        __height (int): The private height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance, validating width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Validate and set __width using the inherited method
        self.integer_validator("width", width)
        self.__width = width

        # Validate and set __height using the inherited method
        self.integer_validator("height", height)
        self.__height = height
