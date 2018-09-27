from exceptions import Empty


class ArrayQueue:
    # first in first out
    DEFAULT_CAPACITY = 10  # capacity for the queue

    def __init__(self):
        """
        Create an empty queue instance
        """
        self.__data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self.__size = 0  # actual number of elements
        self.__front = 0  # index of the front element

    def __len__(self):
        return self.__size

    def is_Empty(self):
        """Return true if list is empty"""
        return self.__size == 0
