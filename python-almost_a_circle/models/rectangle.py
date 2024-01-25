#!/usr/bin/python3
"""
Module for Rectangle sub-class definition
"""
from models.base import Base

class Rectangle(Base):
    """
    Rectangle class definition - inherits from Base

    Attributes:
        __width (int) : private attribute representing width
        __height (int) : private attribute representing height
        __x (int) : private attribute representing x coordinate
        __Y (int) : private attribute representing y coordinate
    """


    def __init__(self, width, height, x=0, y=0, id=None):
