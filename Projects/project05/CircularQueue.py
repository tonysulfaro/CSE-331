"""
# Project 5 - Circular Queue
# Name: Tony Sulfaro
# PID: A52995491
"""


class CircularQueue():
    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0

    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size

    # -----------MODIFY BELOW--------------

    def __str__(self):
        """
        string representation of CircularQueue
        :return: str - representation of CircularQueue
        """
        out = ''
        out += 'size: ' + str(self.size) + '\n'
        out += 'capacity: ' + str(self.capacity) + '\n'
        out += 'head: ' + str(self.head) + '\n'
        out += 'tail: ' + str(self.tail) + '\n'
        out += str(self.data)
        return out

    def is_empty(self):
        """
        Returns if queue is empty or not
        :return: bool - if self.size is 0 (empty)
        """
        return self.size == 0

    def __len__(self):
        """
        Returns the size of the queue (number of elements stored)
        :return: int - self.size
        """
        return self.size

    def first_value(self):
        """
        Gets head value
        :return: int - head value
        """
        return self.data[self.head]

    def enqueue(self, val):
        """
        Adds element to queue
        :param val: int - element to be added
        :return: None
        """
        # add new item in
        self.data[self.tail] = val
        self.size += 1

        if self.size == self.capacity:
            self.grow()

        self.tail = (self.size + self.head) % self.capacity

    def dequeue(self):
        """
        Pop element from front of queue
        :return: int - popped element
        """
        # don't pop an empty queue
        if self.size == 0:
            return

        # get popped item and adjust object attributes
        popped = self.data[self.head]
        self.data[self.head] = None
        self.size -= 1
        self.head = (self.head + 1) % self.capacity

        # check weather to shrink
        if self.size >= 1:
            if self.capacity / self.size >= 4:
                self.shrink()

        return popped

    def grow(self):
        """
        Increases self.data capacity by 2
        :return: None
        """
        # initialize new array to put values in
        temp = [None] * (self.size * 2)

        # copy over ones starting at the head
        for x in range(self.head, self.capacity):
            temp[x - self.head] = self.data[x]
        # copy over ones up til the head if they exist
        for x in range(0, self.head):
            temp[x + self.capacity - self.head] = self.data[x]

        # adjust object attributes
        self.head = 0
        self.tail = self.size
        self.data = temp
        self.capacity *= 2

    def shrink(self):
        """
        Decreases self.capacity by 2 when it is using 1/4 of its total capacity
        :return: None
        """
        # don't shrink if it will be less than 4
        if self.capacity < 8:
            return

        # initialize new reduced size list
        temp = [None] * (self.capacity // 2)

        # add in values from head to capacity if they are not none
        for x in range(self.head, self.capacity):
            if self.data[x] is not None:
                temp[x - self.head] = self.data[x]
        # if there are values before the head when head != 0 add them
        if self.tail < self.head:
            for x in range(0, self.tail):
                temp[self.size - self.tail] = self.data[x]

        # update object attributes
        self.data = temp
        self.tail = self.size
        self.head = 0
        self.capacity //= 2


def main():
    test = CircularQueue(8)
    test.enqueue(1)
    test.dequeue()
    test.enqueue(2)
    test.dequeue()
    test.enqueue(3)
    test.dequeue()
    test.enqueue(4)
    test.dequeue()
    test.enqueue(5)
    test.dequeue()
    test.enqueue(6)
    test.dequeue()
    test.enqueue(7)
    test.dequeue()
    test.enqueue(8)
    # test.enqueue(9)
    # test.enqueue(10)
    # test.enqueue(11)
    # test.enqueue(12)
    # test.enqueue(13)
    # test.enqueue(14)

    print(test)

    print('REMOVE')

    # test.dequeue()
    # test.dequeue()
    # test.dequeue()
    # test.dequeue()
    # test.dequeue()
    # test.dequeue()
    # test.dequeue()
    # test.dequeue()

    print(test)


if __name__ == '__main__':
    main()
