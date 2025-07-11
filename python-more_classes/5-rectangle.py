#!/usr/bin/python3
'''
this module 1-rectangle is Real definition of a rectangle
'''


class Rectangle:
    '''
    this module 1-rectangle is Real definition of a rectangle
    '''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return (self.__width + self.__height) * 2

    def __str__(self):
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        for i in range(self.__height):
            result += "#" * self.__width
            if i != self.height - 1:
                result += "\n"
        return result

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
