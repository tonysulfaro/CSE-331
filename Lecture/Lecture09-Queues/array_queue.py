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

    def _resize(self, cap):
        old = self.__data
        self.data = [None]*cap
        walk = self.__front

        for k in range(self.__size):
            self.__data[k] = old[walk]  # normalization, set front to 0
            walk = (1+walk) % len(old)

        self.__front = 0

    def enqueue(self, e):
        if self.__size == len(self.__data):
            self._resize(2*len(self.__data))

        # find the next availible spot on that list
        avail = (self.__front + self.__size) % len(self.__data)

        # put data in right place
        self.__data[avail] = e

        # increment the size by one
        self.__size += 1

    def dequeue(self):
        if self.is_Empty():
            raise Empty('The queue is empty, cant do that')
        answer = self.__data[self.__front]
        self.__data[self.__front] = None  # remove the front, set to null
        self.__front = (self.__front + 1) % len(self.__data)

        # decrement the size
        self.__size -= 1
        return answer
