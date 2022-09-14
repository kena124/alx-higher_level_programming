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

    def my_print(self):
        """ Prints in stdout the square with the character #. """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
