#!/usr/bin/python3
"""
Module 6-rectangle
Defines a class Rectangle and tracks the number of active instances.
This module introduces a class attribute, `number_of_instances`, to demonstrate
how classes can maintain shared state and track the lifecycle of their instances
(incremented in __init__ and decremented in __del__).
"""


class Rectangle:
    """
    The Rectangle class defines a rectangle object and tracks its instance count.
    """

    # Public Class Attribute: Tracks the number of active instances
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance and increments the instance counter.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with validation.

        Args:
            value (int): The width to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with validation.

        Args:
            value (int): The height to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter (2 * (width + height)). Returns 0 if
                 either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns the informal, nicely printable string representation of the Rectangle.

        Prints the rectangle using the character '#'. If width or height is 0,
        it returns an empty string.

        Returns:
            str: A string representing the rectangle structure.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_rows = []
        for _ in range(self.__height):
            rect_rows.append("#" * self.__width)
        return "\n".join(rect_rows)

    def __repr__(self):
        """
        Returns the "official" string representation of the Rectangle.

        The format is designed to be executable by eval() to recreate the instance.

        Returns:
            str: A string in the format "Rectangle(width, height)".
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor method called when an instance is deleted.

        It prints a farewell message and decrements the instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
