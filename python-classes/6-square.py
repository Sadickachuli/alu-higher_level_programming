#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Private instance attribute: size
    Private instance attribute: position
    Instantiation with optional size and optional position:
    Public instance method: def area(self): that returns the square area
    Public instance method: def my_print(self): that prints the square with  #:
        no import modules"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >+ 0")
        else:
            self.__size = value
