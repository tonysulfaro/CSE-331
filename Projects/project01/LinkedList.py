########################################
# PROJECT 1 - Linked List
# Author: Tony Sulfaro
# PID: A52995491
########################################


class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'next_node'

    def __init__(self, value, next_node=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next_node: pointer to the next node, default is None
        """
        self.value = value  # element at the node
        self.next_node = next_node  # reference to next node

    def __eq__(self, other):
        """
        DO NOT EDIT
        Determine if two nodes are equal (same value)
        :param other: node to compare to
        :return: True if nodes are equal, False otherwise
        """
        if other is None:
            return False
        if self.value == other.value:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)


class LinkedList:
    def __init__(self):
        """
        DO NOT EDIT
        Create/initialize an empty linked list
        """
        self.head = None   # Node
        self.tail = None   # Node
        self.size = 0      # Integer

    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """
        if self.size != other.size:
            return False
        if self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other:
                temp_self = temp_self.next_node
                temp_other = temp_other.next_node
            else:
                return False
        # Make sure other is not longer than self
        if temp_self is None and temp_other is None:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a linked list
        :return: string of list of values
        """
        temp_node = self.head
        values = []
        if temp_node is None:
            return None
        while temp_node is not None:
            values.append(temp_node.value)
            temp_node = temp_node.next_node
        return str(values)

    ###### MODIFY THE BELOW FUNCTIONS #####

    # ------------------------Accessor Functions---------------------------

    def length(self):
        """
        Gets the number of nodes of the linked list
        :return: size of list
        """
        return self.size


    def is_empty(self):
        """
        Determines if the linked list is empty
        :return: True if list is empty and False if not empty
        """
        return self.size == 0


    def front_value(self):
        """
        Gets the first value of the list
        :return: value of the list head
        """
        if self.head is not None:
            return self.head.value
        return None


    def back_value(self):
        """
        Gets the last value of the list
        :return: value of the list tail
        """
        if self.tail is not None:
            return self.tail.value
        return None


    def count(self, val):
        """
        Counts the number of times a value 'val' occurs in the list
        :param val: value to find and count
        :return: number of time 'val' occurs
        """
        count = 0
        temp_self = self.head

        if temp_self is None:
            return 0

        while temp_self is not None:
            if temp_self.value == val:
                count += 1
            temp_self = temp_self.next_node
        return count


    def find(self, val):
        """
        Searches for and returns the first node with the value 'val'
        :param val: value to search for
        :return: True if value is in list, False if value is not found
        """
        temp_self = self.head
        while temp_self is not None:
            if temp_self.value == val:
                return True
            temp_self = temp_self.next_node
        return False

    # ------------------------Mutator Functions---------------------------

    def push_front(self, val):
        """
        Adds a node to the front of the list with value 'val'
        :param val: value to add to list
        :return: no return
        """
        if self.size == 0:
            new_node = Node(val, self.head)
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.head = Node(val, self.head)
            self.size += 1


    def push_back(self, val):
        """
        Adds a node to the back of the list with value 'val'
        :param val: value to add to list
        :return: no return
        """
        if self.size == 0:
            new_node = Node(val)
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node = Node(val)
            self.tail.next_node = new_node
            self.tail = new_node
            self.size += 1


    def pop_front(self):
        """
        Removes a node from the front of the list
        :return: the value of the removed node
        """

        head = self.head
        if head is not None:
            next_node = self.head.next_node

            if head is not None:
                self.head = next_node
                self.size -= 1

            return head.value
        else:
            return None


    def pop_back(self):
        """
        Removes a node from the back of the list
        :return: the value of the removed node
        """

        if self.head is not None:

            current_node = self.head
            prev_node = None

            while current_node.next_node is not None:
                prev_node = current_node
                current_node = current_node.next_node

            if prev_node is None: # popping list of one element
                self.head = None
                self.tail = None
                self.size -= 1
                return current_node.value
            else:
                prev_node.next_node = None
                self.tail = prev_node
                self.size -= 1
                return current_node.value

        else:
            return None


    def reverse_list(self):
        """
        Reverses the values of the given linked list
        :return: no return
        """
        current_node = self.head
        prev_node = None
        self.tail = self.head

        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

def main():
    """
    Main Docstring
    :return: no return
    """

    stu = LinkedList()

    stu.push_front(45)
    stu.push_front(39)
    stu.push_front(10)
    stu.push_front(98)
    stu.push_front(6)

    print(stu)
    print('size: ', stu.size)
    print('head: ', stu.head.value)
    print('tail: ', stu.tail.value)
    
    stu.reverse_list()
    print(stu)
    print('size: ', stu.size)
    print('head: ', stu.head.value)
    print('tail: ', stu.tail.value)

    '''current_node = stu.head
    while current_node.next_node is not None:
        print('node: ', current_node.value,' next: ', current_node.next_node.value)
        current_node =  current_node.next_node'''
    

if __name__ == "__main__":
    main()