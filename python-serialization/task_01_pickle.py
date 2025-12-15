#!/usr/bin/python3
import os
import pickle
class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}\nAge: {}\nIs Student: {}".format(
            self.name, self.age, self.is_student))

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            return True
        except Exception as e:
            return False
    @classmethod
    def deserialize(cls, filename):
        try:
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File not found: {filename}")
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError, Exception):
            return None
