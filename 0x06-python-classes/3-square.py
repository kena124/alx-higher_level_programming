#!/usr/bin/python3

""" Object Oriented Programming Fundamental module """


class Square:
    """ The object representation of a square with size attribute """
    def __init__(self, size=0):

        self.isValidSize(size)
        self.__size = size

    def isValidSize(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
