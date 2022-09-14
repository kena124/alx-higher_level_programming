#!/usr/bin/python3

""" Object Oriented Programming Fundamental module """


class Square:
    """ The object representation of a square with size attribute """
    def __init__(self, size=0, position=(0, 0)):
        self.isValidSize(size)
        self.__size = size

        self.isValidPosition(position)
        self.__position = position

    def isValidSize(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def isValidPosition(self, position):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) or\
           not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Calculate and return the area of the square. """
        return self.__size * self.__size

    @property
    def size(self):
        """ Return the size of the square. """
        return self.__size

    @property
    def position(self):
        """ Return the  position of the square. """
        return self.__position

    @size.setter
    def size(self, value):
        """ Sets the size value of the square. """
        self.isValidSize(value)
        self.__size = value

    @position.setter
    def position(self, value):
        self.isValidPosition(value)
        self.__position = value

    def my_print(self):
        """ Prints in stdout the square with the character #. """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
