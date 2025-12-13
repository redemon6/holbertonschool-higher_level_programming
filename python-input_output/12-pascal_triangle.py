#!/usr/bin/python3
"""
Module 12-pascal_triangle
Defines a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows of the triangle to generate.

    Returns:
        list: A list of lists of integers representing the triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Initialize the current row
        current_row = []

        # The first element of every row is 1
        current_row.append(1)

        if i > 0:
            # Get the previous row
            prev_row = triangle[-1]

            # Calculate intermediate elements
            # Iterate from the second element up to (but not including) the 
            for j in range(1, i):
                # The value is the sum of the two elements above it in the 
                next_value = prev_row[j - 1] + prev_row[j]
                current_row.append(next_value)

            # The last element of every row is 1
            current_row.append(1)

        # Add the completed row to the triangle
        triangle.append(current_row)

    return triangle
