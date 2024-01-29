#!/usr/bin/python3
"""
Module for Base class definition
"""
import json


class Base:
    """
    Base class definition

    Attributes:
        __nb_objects (int) : private class attribute to manage ID
        id (int) : public attribute representing object's ID #
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of Base class

        Args:
            id (int) : If provided, assigns ID attribute to this value
            If not provided, automatically generates an ID
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1  # increment # of instances count
            self.id = Base.__nb_objects  # assign count to ID #

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method called before instantiation that
        returns JSON representation of key:value pairs
        of all Base instances

        Args:
            list_dictionaries : list of dictionaries of class Base

        Return:
        JSON string representation of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
