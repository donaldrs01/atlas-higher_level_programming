#!/usr/bin/python3
"""
Module for BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """
        Incomplete method that raises Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the passed value

        Args:
            name : the name of the value (str)
            value : the value (int)

        Raises:
            TypeError : if value is not integer
            ValueError : if value is less than or equal to 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
