#!/usr/bin/python3
"""
Module 1-my_list
Defines a class MyList that inherits from the built-in list type.
"""


class MyList(list):
    """
    MyList class inherits from list.

    It provides one additional public instance method: print_sorted.
    """
    def print_sorted(self):
        """
        Prints the list elements in ascending sorted order.

        It creates a new sorted list for printing and does not modify
        the original list instance. Assumes all elements are integers.
        """
        print(sorted(self))
