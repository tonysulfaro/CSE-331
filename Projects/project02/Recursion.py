"""
PROJECT 2 - Recursion
Name: Tony Sulfaro
PID: A52995491
"""

from LinkedNode import LinkedNode


def insert(value, node=None):

    if node is None or not node.value < value:
        return LinkedNode(value, None)

    node.next_node = insert(value, node.next_node)

    return node


def string(node):

    if node is not None and node.next_node:  # first or n-1 element in the linked list
        return str(node.value) + ", " + string(node.next_node)

    if node.next_node is None:  # last element in linked list
        return str(node.value)

    return ''


def reversed_string(node):

    if node is not None and node.next_node:
        return reversed_string(node.next_node) + ", " + str(node.value)

    if node.next_node is None:
        return str(node.value)

    return ''


def remove(value, node):

    if node.next_node.value == value:
        node.next_node = node.next_node.next_node
        return

    return remove(value, node.next_node)


def remove_all(value, node):

    if node.value == value:
        print('hmm')

    return remove_all(value, node.next_node)


def search(value, node):

    if node is not None:
        if node.value == value:
            return True
        return search(value, node.next_node)

    return False


def length(node):

    if node is not None:
        return 1 + length(node.next_node)

    return 0


def sum_all(node):

    if node is not None:
        return node.value + sum_all(node.next_node)

    return 0


def count(value, node):

    if node is not None:
        if value == node.value:
            return 1 + count(value, node.next_node)
        return count(value, node.next_node)

    return 0


def main():

    linked_node = insert(1, None)

    insert(2, linked_node)
    insert(3, linked_node)
    insert(4, linked_node)
    insert(5, linked_node)

    print(sum_all(linked_node))
    print(length(linked_node))
    print(count(9, linked_node))
    print(search(0, linked_node))
    print(string(linked_node))
    print(reversed_string(linked_node))


if __name__ == '__main__':
    main()
