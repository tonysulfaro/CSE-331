"""
PROJECT 2 - Recursion
Name: Tony Sulfaro
PID: A52995491
"""

from LinkedNode import LinkedNode


def insert(value, node=None):

    if node is None or node.value > value:
        return LinkedNode(value, None)

    node.next_node = insert(value, node.next_node)

    return node


def string(node):

    output = ""

    output += str(node.value)
    output += ', '

    if node.next_node is None:
        return output[:-2]

    return string(node.next_node)


def reversed_string(node):
    pass


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

    if node.value == value:
        return True

    if node.next_node is not None:
        return search(value, node.next_node)

    return False


def length(node):

    num = 0

    if node is not None:
        num += 1

    if node.next_ndoe is not None:
        return length(node.next_node)

    return num


def sum_all(node):

    if node is not None:
        return node.value + sum_all(node.next_node)

    return 0


def count(value, node):

    num = 0

    if node.value == value:
        num += 1

    return count(value, node.next_node)


def main():

    linked_node = insert(1, None)

    linked_node = insert(2, linked_node)
    linked_node = insert(3, linked_node)
    linked_node = insert(4, linked_node)
    linked_node = insert(5, linked_node)

    node = linked_node
    while node is not None:
        print(node.value)
        node = node.next_node


if __name__ == '__main__':
    main()
