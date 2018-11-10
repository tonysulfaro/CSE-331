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
        pass

    def parent(self, position):
        pass

    def left_child(self, position):
        pass

    def right_child(self, position):
        pass

    def has_left(self, position):
        pass

    def has_right(self, position):
        pass

    def find(self, value):
        pass

    def heap_push(self, value):
        pass

    def heap_pop(self, value):
        pass

    def pop_min(self):
        pass

    def swap(self, p1, p2):
        pass

    def percolate_up(self, position):
        pass

    def percolate_down(self, position):
        pass


def heap_sort(unsorted):
    pass
