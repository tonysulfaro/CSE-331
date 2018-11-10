########################################
# PROJECT: Binary Min Heap and Sort
# Author: Tony Sulfaro
########################################


class BinaryMinHeap:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self):
        """
        Creates an empty hash table with a fixed capacity
        """
        self.table = []

    def __eq__(self, other):
        """
        Equality comparison for heaps
        :param other: Heap being compared to
        :return: True if equal, False if not equal
        """
        if len(self.table) != len(other.table):
            return False
        for i in range(len(self.table)):
            if self.table[i] != other.table[i]:
                return False

        return True

    ###### COMPLETE THE FUNCTIONS BELOW ######

    def __str__(self):
        pass

    def get_size(self):
        return len(self.table)

    def parent(self, position):
        return (position - 1) // 2

    def left_child(self, position):
        return 2 * position + 1

    def right_child(self, position):
        return 2 * position + 2

    def has_left(self, position):
        return self.left_child(position) is not None

    def has_right(self, position):
        return self.right_child(position) is not None

    def find(self, value):
        for x in range(len(self.table)):
            if self.table[x] == value:
                return x

    def heap_push(self, value):
        if self.find(value) is None:
            self.table.append(value)
            self.percolate_up(len(self.table) - 1)

    def heap_pop(self, value):
        pass

    def pop_min(self):
        pass

    def swap(self, p1, p2):
        self.table[p1], self.table[p2] = self.table[p2], self.table[p1]

    def percolate_up(self, position):

        parent = self.parent(position)
        if position > 0 and self.table[position] < self.table[parent]:
            self.swap(position, parent)
            self.percolate_up(parent)

    def percolate_down(self, position):

        if self.has_left(position):
            left = self.left_child(position)
            small_child = left
            if self.has_right(position):
                right = self.right_child(position)
                if self.table[right] < self.table[left]:
                    small_child = right

            if self.table[small_child] < self.table[position]:
                self.swap(position, small_child)
                self.percolate_down(small_child)


def heap_sort(unsorted):
    pass
