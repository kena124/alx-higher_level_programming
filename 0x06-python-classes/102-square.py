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
        """ Calculate and return the area of the square. """
        return self.__size * self.__size

    @property
    def size(self):
        """ Return the size of the square. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size value of the square. """
        self.isValidSize(value)
        self.__size = value

    def __gt__(self, other):
        """ Return if self is greater than other. """
        return self.size > other.size

    def __ge__(self, other):
        """ Returns if self is greater or equal. """
        return self.size >= other.size

    def __eq__(self, other):
        """ Returns if self and other are equal. """
        return self.size == other.size

    def __ls__(self, other):
        """ Returns if self is less than other. """
        return self.size < other.size

    def __le__(self, other):
        """ Returns if self is less or equal with other. """
        return self.size <= other.size
