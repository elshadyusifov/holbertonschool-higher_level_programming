#!/usr/bin/python3
'''
this module 1-rectangle is Real definition of a rectangle
'''


class Rectangle:
    '''
    this module 1-rectangle is Real definition of a rectangle
    '''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    
    @property
    def __width(self):
        return self.__width
    
    @__width.setter
    def __width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def __height(self):
        return self.__height
    
    @__height.setter
    def __height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
