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
        if self.size == 0:
            return
        popped = self.data[self.head]
        self.data[self.head] = None
        self.size -= 1
        self.head += 1

        if self.head == self.tail:
            self.head = 0
            self.tail = 0
            self.size = 0

        if self.size >= 1:
            if self.capacity / self.size >= 4:
                self.shrink()

        return popped

    def grow(self):
        """
        Increases self.data capacity by 2
        :return: None
        """
        temp = [None] * (self.size * 2)

        for x in range(self.head, self.capacity):
            temp[x - self.head] = self.data[x]
        for x in range(0, self.head):
            temp[x + self.capacity - self.head] = self.data[x]

        self.head = 0
        self.tail = self.size

        self.data = temp
        self.capacity *= 2

    def shrink(self):
        """
        Decreases self.capacity by 2 when it is using 1/4 of its total capacity
        :return: None
        """
        if self.capacity < 8:
            return

        temp = [None] * (self.capacity // 2)

        for x in range(self.head, self.tail):
            temp[x - self.head] = self.data[x]

        self.data = temp
        self.tail = self.size
        self.head = 0
        self.capacity //= 2


def main():
    test = CircularQueue(8)
    test.enqueue(3)
    test.enqueue(3)
    test.enqueue(3)
    test.enqueue(3)
    test.enqueue(3)
    test.enqueue(3)
    test.enqueue(3)
    test.enqueue(3)

    print(test)

    print('REMOVE')

    test.dequeue()
    test.dequeue()
    test.dequeue()
    test.dequeue()
    test.dequeue()
    test.dequeue()
    test.enqueue(5)
    test.enqueue(5)
    test.enqueue(5)
    test.enqueue(5)
    test.dequeue()
    # test.dequeue()
    # test.dequeue()
    # test.dequeue()
    # test.dequeue()

    print(test)


if __name__ == '__main__':
    main()
