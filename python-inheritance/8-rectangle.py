#!/usr/bin/python3
"""
Module 8-rectangle
Defines a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
and uses the inherited integer_validator for attribute validation.
"""


class BaseGeometry:
    """
    A base class for geometric shapes, providing an interface for area
    and a utility method for validating integer values.
    """
    def area(self):
        """
        Public instance method that raises an exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer. The message is
                       "<name> must be an integer".
            ValueError: If value is less than or equal to 0. The message is
                        "<name> must be greater than 0".
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
