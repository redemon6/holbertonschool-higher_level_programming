#!/usr/bin/python3
"""
Module 10-student
Defines a class Student with filtering capability for its dictionary repr.
"""


class Student:
    """
    Represents a student with a first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiates a new Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes named in the list
        that exist in the instance are included in the dictionary.
        Otherwise, all public attributes are retrieved.

        Args:
            attrs (list, optional): A list of strings representing the
                                    attribute names to retrieve. Default = Non

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            # If attrs is a list of strings, filter the dictionary
            filtered_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    filtered_dict[key] = getattr(self, key)
            return filtered_dict
        
        # Otherwise, return all public instance attributes
        # __dict__ retrieves all attributes set on the instance (which public)
        return self.__dict__
