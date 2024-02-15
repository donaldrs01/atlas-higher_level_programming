#!/usr/bin/python3
"""
Module containing BaseGeometry class and Rectangle subclass
"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """
        Incomplete method that raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the passed value

        Args:
            name : name of value (str)
            value : the value (int)

        Raises:
            TypeError : if value not integer
            ValueError : if valuee is less than or equal to 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Class definition of rectangle - subclass
    """
    def __init__(self, width, height):
        """
        Method that initializes Rectangle instance

        Args:
            width : width of rectangle
            height : height of rectangle
        """
        super().__init__()
        # validate and set width and height #
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Finds area of rectangle

        Returns:
            area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns string representation of rectangle

        Return:
            Rectangle (str representation)
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
