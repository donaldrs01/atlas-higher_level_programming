#!/usr/bin/python3
"""
Module that continues with Rectangle class
"""


class Rectangle:
    """
    Rectangle class with width and height attributes
    """
    number_of_instances = 0  # establish counter attribute
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Init method for Rectangle

        Args:
            width (int) : width of rectangle
            height (int) : height of rectangle
        """
        self.width = width
        # defined attribute 'width' that is equal to width passed into method
        self.height = height
        Rectangle.number_of_instances += 1
        # adds 1 to counter for each instantiation

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute

        Args:
            value (int) : value of new rectangle's width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter for height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height

        Args:
            value (int) : value of new rectangle's height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Method for area calculation of rectangle

        Return:
            area of the rectangle
        """
        return self.__width * self.__height
        # area = width * height for rectangle

    def perimeter(self):
        """
        Method for perimeter calculation of rectangle

        Return:
            perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def print(self):
        """
        Method that prints rectangle using '#' character

        Return:
            printed rectangle
        """
        if self.__width == 0 or self.__height == 0:
            print()
            return
        else:
            for i in range(self.height):
                for j in range(self.width):
                    print(self.print_symbol, end="")  # no \n

    def __str__(self):
        """
        Method for string representation of rectangle

        Return:
            string representation of rectangle using '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join([str(self.print_symbol) * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Representation of the rectangle

        Return:
            Representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes an instance of Rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        # removes 1 from counter for each deletion

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that compares two rectangles based on area

        Args:
            rect_1 (Rectangle) : first rectangle
            rect_2 (Rectangle) : second rectangle

        Return:
            The rectangle with the bigger area
            (returns rect_1 if areas are equal)
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod  # method bound to class, not specific instance
    def square(cls, size=0):
        """
        Class method that returns new rectangle where width = height = size

        Args:
            cls (class): the class (Rectangle) itself
            size (int) : the size of the width and height of new rectangle

        Return:
            Rectangle : a new instance of rectangle with equal size/width/height
        """
        return cls(size, size)
        #  creates and returns new Rectangle with width/height set to size value
