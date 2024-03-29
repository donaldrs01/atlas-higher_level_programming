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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes and saves a JSON
        string to file <Class name>.json

        Args:
            cls : represents class itself
            list_objs : list of instances of that class
        """
        if list_objs is None:
            list_objs = []
        else:
            list_objs = [obj.to_dictionary() for obj in list_objs]
            # list comprehension for method call on to_dictionary
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))
            #  writes to file by calling to_json_string

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that deserializes JSON string
        and converts into dictionary

        Args:
            json_string : JSON-formatted string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """
        Class method that loads instances from file by
        converting JSON string into list of dicts and then
        creating instances from these values
        """
        from os import path
        file = "{}.json".format(cls.__name__)  # construct filename to search
        if not path.isfile(file):  # checks if file exists
            return []  # returns empty list if not
        with open(file, "r", encoding="utf-8") as f:  # opens and reads
            jstr = f.read()
            return [cls.create(**dict) for dict in cls.from_json_string(jstr)]
            #  creates instances for each dict in list

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that takes dictionary pairs (kwargs) of class
        and creates instances with those values

        Args:
            cls : represents class itself
            **dictionary : variable number of keyword args representing
            key/value pairs
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            dummy = Rectangle(2, 1)
        elif cls is Square:
            dummy = Square(4)
        else:
            dummy = None

        dummy.update(**dictionary)
        #  update dummy instance with dict values

        return dummy
