#!/usr/bin/python3
"""
Module 11-student
Defines a class Student with methods for serialization (to_json) and
deserialization (reload_from_json).
"""


class Student:
    """
    Represents a student with a first name, last name, and age.

    Implements methods for converting the instance to a dictionary and
    reloading the instance's attributes from a dictionary.
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
        Retrieves a dictionary representation of the Student instance,
        optionally filtered by a list of attributes.

        Args:
            attrs (list, optional): A list of strings representing the
                                    attribute names to retrieve. Default None.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            # Filter based on the provided list of strings
            filtered_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    filtered_dict[key] = getattr(self, key)
            return filtered_dict
        # Return all public instance attributes (which are all set here)
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.

        This method iterates through the provided dictionary (json) and
        uses the key as the attribute name and the value as the new
        attribute value for the instance.

        Args:
            json (dict): A dictionary where keys are attribute names and
                         values are the new attribute values.
        """
        # Iterate over the key-value pairs in the provided dictionary
        for key, value in json.items():
            # Use setattr() to set the new attribute on the current instance
            setattr(self, key, value)
