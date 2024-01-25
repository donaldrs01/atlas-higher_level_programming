#!/usr/bin/python3
"""
Module for Base class definition
"""


class Base:
    """
    Base class definition

    Attributes:
        __nb_objects (int) : private class attribute to manage ID
        id (int) : public attribute representing object's ID #
    """
    __nb_objects = 0

    def__init__(self, id=None):
        """
        Initializes a new instance of Base class

        Args:
            id (int) : If provided, assigns ID attribute to this value
            If not provided, automatically generates an ID
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
