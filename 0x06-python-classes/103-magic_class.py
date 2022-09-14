#!/usr/bin/python3

""" Bytecode reversing with object oriented program. """
import math


class MagicClass:
    """ Magic class that represent a circle. """
    def __init__(self, radius=0):
        self.__radius = 0

        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """ Returns the area of the circle. """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ Returns the circumference of the circle. """
        return 2 * math.pi * self.__radius
