#!/usr/bin/python3
"""
Module 8-rectangle
Defines a class Rectangle with a static method for comparing areas.
This module introduces a static method, `bigger_or_equal`, to demonstrate
a utility function related to the class that does not require instance access,
but still operates on Rectangle objects.
"""


class Rectangle:
    """
    The Rectangle class defines a rectangle object, tracking its instance
    count,providing a customizable symbol for printing, and including a static
    method for comparison.
    """

    # Public Class Attribute: Tracks the number of active instances
    number_of_instances = 0

    # Public Class Attribute: Used as the symbol for string representation
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance and increments the instance
        counter.
        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0
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
        Returns the informal, nicely printable string representation of the
        Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)

        rect_rows = []
        for _ in range(self.__height):
            rect_rows.append(symbol * self.__width)
        return "\n".join(rect_rows)

    def __repr__(self):
        """
        Returns the "official" string representation of the Rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor method called when an instance is deleted.

        It prints a farewell message and decrements the instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the one with the largest area.

        If the areas are equal, it returns rect_1.

        Args:
            rect_1 (Rectangle): The first rectangle instance.
            rect_2 (Rectangle): The second rectangle instance.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle instance with the larger or equal area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
