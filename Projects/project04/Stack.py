"""
# Project 4
# Name: Tony Sulfaro
# PID: A52995491
"""

class Stack:
    """
    Stack class
    """
    def __init__(self, capacity=2):
        """
        DO NOT MODIFY
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack. Default size 2.
        """
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0

    def __str__(self):
        """
        DO NOT MODIFY
        Prints the values in the stack from bottom to top. Then, prints capacity.
        :return: string
        """
        if self.size == 0:
            return "Empty Stack"

        output = []
        for i in range(self.size):
            output.append(str(self.data[i]))
        return "{} Capacity: {}".format(output, str(self.capacity))

    def __eq__(self, stack2):
        """
        DO NOT MODIFY
        Checks if two stacks are equivalent to each other. Checks equivalency of data and capacity
        :return: True if equal, False if not
        """
        if self.capacity != stack2.capacity:
            return False

        count = 0
        for item in self.data:
            if item != stack2.data[count]:
                return False
            count += 1

        return True

    def stack_size(self):
        """
        returns size of stack
        :return: int size
        """
        return self.size

    def is_empty(self):
        """
        checks if stack is empty
        :return: bool
        """
        return self.size == 0

    def top(self):
        """
        gets item at top of stack
        :return: top of stack
        """
        return self.data[-1]

    def push(self, val):
        """
        add new value into stack
        :param val: value to be added to top of stack
        :return: None
        """
        if self.size == self.capacity:
            self.grow()
        self.data[self.size] = val
        self.size += 1

    def pop(self):
        """
        pop last element out of stack
        :return: popped item if it exists, None otherwise
        """
        if self.size == 0:
            return None
        self.size -= 1
        return self.data.pop()

    def grow(self):
        """
        increases stack capacity by factor of 2
        :return: None
        """
        temp = self.data
        self.size *= 2
        self.data = [None] * self.size

        for item in temp:
            self.data.append(item)

    def shrink(self):
        """
        Shrinks list capacity by factor of 2
        :return: None
        """
        temp = self.data
        self.size /= 2
        self.data = [None] * self.size

        for item in temp:
            self.data.append(item)


def reverse(stack):
    """
    Reverses stack using a queue
    :param stack: Stack to be reversed
    :return: Reversed Stack
    """
    return reverse(stack)


def replace(stack, old, new):
    """
    Replace values in old stack with that of the new one
    :param stack: Stack to do replacing on
    :param old: old value to search for
    :param new: new value to replace it with
    :return: Stack of replaced values
    """
    new_stack = [None] * stack.size
    for item in stack:
        if item == old:
            new_stack.append(new)
        new_stack.append(item)
