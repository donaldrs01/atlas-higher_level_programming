#!/usr/bin/python3
"""
Module for Student class definition
"""


class Student:
    """
    Student class

    Attributes:
        first_name
        last_name
        age

    Methods:
        def to_json(self)  :
            returns dictionary representation of instance of Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes new instance of Student

        Args:
            first_name (str) : first name of student
            last_name (str) : last name of student
            age (int) : age of student
        """
        self.first_name = first_name  # initializes attributes based on input
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Provides dict representation of instance of Student

        Args:
            attrs (list) : List of attribute names to be retrieved

        Returns:
            dict : dictionary representation of Student instance
        """
        if attrs is None:
            return self.__dict__
        #  returns all attributes of instance if none specified

        filtered_dict = {}  # only includes attributes passed as input
        for attribute in attrs:
            if hasattr(self, attribute):  #  utilize hasattr builtin
                filtered_dict[attribute] = getattr(self, attribute)
        return filtered_dict
