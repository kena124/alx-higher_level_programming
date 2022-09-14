#!/usr/bin/python3

""" Singly linked list data structure implementation. """


class Node:
    """ A class Node that defines a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ Returns the data value. """
        return self.__data

    @property
    def next_node(self):
        """ Returns the next_node value. """
        return self.__next_node

    @data.setter
    def data(self, value):
        """ Updates the value of data. """
        if not isinstance(value, data):
            raise TypeError("data must be integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """ Updates the value of the next_node. """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ A class SinglyLinkedList that defines a singly linked list. """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a new Node into the correct
        sorted position in the list increasing order. """
        new_node = Node(value)
        cur = self.__head
        prev = None

        while cur is not None:
            if cur.data >= new_node.data:
                break
            prev = cur
            cur = cur.next_node

        new_node.next_node = cur
        if prev is None:
            self.__head = new_node
        else:
            prev.next_node = new_node

    def __str__(self):
        """ Returns the data in printable string. """
        cur = self.__head
        result = ""

        while cur is not None:
            result += str(cur.data)
            cur = cur.next_node

            if cur is not None:
                result += "\n"
        return result
