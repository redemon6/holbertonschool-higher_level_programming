#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a class BaseGeometry with an unimplemented area method and
a method for validating integer values.
"""


class BaseGeometry:
    """
    A base class for geometric shapes.

    Includes methods for area implementation enforcement and integer validate.
    """
    def area(self):
        """
        Public instance method that raises an exception.

        This method is meant to be overridden in subclasses.

        Raises:
            Exception: Always raises an Exception with the message
                       "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the value (assumed to be a string).
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
