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
        """
        gets size of table
        :return: integer - table size
        """
        return len(self.table)

    def parent(self, position):
        """
        gets parent position
        :param position: integer - child position
        :return: integer - parent position in table
        """
        return (position - 1) // 2

    def left_child(self, position):
        """
        gets left child for parent if exists
        :param position: integer - parent location
        :return: integer - left child location
        """
        child = 2 * position + 1
        if child > len(self.table) - 1:
            return None
        return child

    def right_child(self, position):
        """
        gets right child for parent if exists
        :param position: integer - parent location
        :return: integer - right child location
        """
        child = 2 * position + 2
        if child > len(self.table) - 1:
            return None
        return child

    def has_left(self, position):
        """
        checks if left child exists
        :param position: integer - parent location
        :return: bool - if left child exists
        """
        return self.left_child(position) is not None

    def has_right(self, position):
        """
        checks if right child exists
        :param position: integer - parent location
        :return: bool - if right child exists
        """
        return self.right_child(position) is not None

    def find(self, value):
        """
        search for value in table, return item index if exists
        :param value: integer - value to search for
        :return: integer - item index
        """
        for position in range(self.get_size()):
            if self.table[position] == value:
                return position

    def heap_push(self, value):
        """
        add item to min heap
        :param value: value to push onto heap
        :return: no return
        """
        if self.find(value) is None:
            self.table.append(value)
            self.percolate_up(self.get_size() - 1)

    def heap_pop(self, value):
        """
        pop specified value from heap them promote children if applicable
        :param value: value to remove from heap
        :return: no return
        """
        if value is None or self.get_size() == 0:
            return

        if self.find(value) is not None:
            # end of list
            position = self.find(value)
            last = self.get_size() - 1

            # pop element and percolate down
            self.swap(position, last)
            self.table.pop()
            self.percolate_down(position)
            return

    def pop_min(self):
        """
        remove min item from heap, pop root essentially
        :return: item popped from heap
        """
        if self.get_size() == 0:
            return None

        # put minimum item at the end
        self.swap(0, len(self.table) - 1)

        # and remove it from the list;
        item = self.table.pop()

        # then fix new root
        self.percolate_down(0)
        return item

    def swap(self, p1, p2):
        """
        swap elements in heap, (usually parent,child swaps)
        :param p1: integer - first item index
        :param p2: integer - second item index
        :return: no return
        """
        self.table[p1], self.table[p2] = self.table[p2], self.table[p1]

    def percolate_up(self, position):
        """
        promote node until its children are greater than it
        :param position: integer - position to start percolation up
        :return: no return
        """
        parent = self.parent(position)
        if position > 0 and self.table[position] < self.table[parent]:  # not root and child > parent
            self.swap(position, parent)
            self.percolate_up(parent)  # recurse

    def percolate_down(self, position):
        """
        demote node until it is greater than its parent
        :param position: integer - position to start percolation down
        :return: no return
        """
        if self.has_left(position):

            left = self.left_child(position)
            small_child = left
            if self.has_right(position):
                right = self.right_child(position)
                if self.table[right] < self.table[left]:
                    small_child = right

            # swap smaller element up then do again until it cant go down anymore
            if self.table[small_child] < self.table[position]:
                self.swap(position, small_child)
                self.percolate_down(small_child)


def heap_sort(unsorted):
    """
    sorts list using a min heap
    :param unsorted: list - unsorted list to be sorted
    :return: sorted_list - sorted list of elements with only UNIQUE items
    """
    heap = BinaryMinHeap()

    # add items to heap
    for item in unsorted:
        heap.heap_push(item)

    # new list for things to go in
    sorted_list = [0] * (heap.get_size())

    # add sorted elements
    for position in range(heap.get_size()):
        sorted_list[position] = heap.pop_min()
    return sorted_list
