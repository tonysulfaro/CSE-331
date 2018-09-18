"""
PROJECT 2 - Recursion
Name: Tony Sulfaro
PID: A52995491
"""

from LinkedNode import LinkedNode


def insert(value, node=None):
    """
    Insert new value into linked list
    :param value: value of new node in list
    :param node: value of next node
    :return: node: head of linked list
    """

    if node is None:
        return LinkedNode(value, None)

    if node.value >= value:
        return LinkedNode(value, node)

    node.next_node = insert(value, node.next_node)

    return node


def string(node):
    """
    Print out string representation of linked list
    :param node: value of head node, start of list
    :return: string: string of linked list, comma delimited
    """

    if node is not None and node.next_node is not None:  # first or n-1 element in the linked list
        return str(node.value) + ", " + string(node.next_node)

    elif node is not None:  # last element in list
        return str(node.value)

    return ''


def reversed_string(node):
    """
    Print out string representation of linked list but in reverse order
    :param node: value of head node, start of list
    :return: string: string of linked list, comma delimited
    """

    if node is not None and node.next_node is not None:
        return reversed_string(node.next_node) + ", " + str(node.value)

    elif node.next_node is None and node is not None:
        return str(node.value)

    return ''


def remove(value, node):
    """
    Remove first element that matches value in linked list
    :param value: value to look for
    :param node: value of head node, start of list
    :return: node: linked list head
    """

    if node is not None and node.value == value:
        return node.next_node
    elif node is not None:
        node.next_node = remove(value, node.next_node)

    return node


def remove_all(value, node):
    """
    Remove all elements in linked list that match a value
    :param value: value to look for in list
    :param node: value of head node, start of list
    :return: node: head of linked list
    """

    if node is not None and node.value == value:
        return node.next_node
    elif node is not None:
        node.next_node = remove(value, node.next_node)

    return node


def search(value, node):
    """
    Search for element in the linked list
    :param value: value to look for
    :param node: value of head node, start of list
    :return: bool: weather or not element is in the list
    """

    if node is not None:
        if node.value == value:
            return True
        return search(value, node.next_node)

    return False


def length(node):
    """
    Count how many values there are in the linked list
    :param node: value of head node, start of list
    :return: int: number of list elements
    """

    if node is not None:
        return 1 + length(node.next_node)

    return 0


def sum_all(node):
    """
    Sum all list elements together
    :param node: value of head node, start of list
    :return: int: sum of list elements
    """

    if node is not None:
        return node.value + sum_all(node.next_node)

    return 0


def count(value, node):
    """
    Count number of list elements that match a value
    :param value: value to search for
    :param node: value of head node, start of list
    :return: int: number of elements that match the value
    """

    if node is not None:
        if value == node.value:
            return 1 + count(value, node.next_node)
        return count(value, node.next_node)

    return 0


def main():

    linked_node = insert(5, None)

    linked_node = insert(4, linked_node)
    linked_node = insert(4, linked_node)
    linked_node = insert(4, linked_node)
    linked_node = insert(3, linked_node)
    linked_node = insert(2, linked_node)
    linked_node = insert(1, linked_node)

    print(string(linked_node))
    print(reversed_string(linked_node))

    linked_node = remove(3, linked_node)

    print(string(linked_node))

    linked_node = remove_all(4, linked_node)

    print(string(linked_node))


if __name__ == '__main__':
    main()
