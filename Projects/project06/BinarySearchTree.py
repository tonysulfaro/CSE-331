"""
# Project 6 - Binary Search Tree
# Name: Tony Sulfaro
# PID: A52995491
"""


class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)


class BinarySearchTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    ### Implement/Modify the functions below ###

    def insert(self, value):

        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            cur = self.root
            while cur is not None:
                if new_node.value == cur.value:
                    self.size -= 1
                if new_node.value < cur.value:
                    if cur.left is None:
                        new_node.parent = cur
                        cur.left = new_node
                        cur = None
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        new_node.parent = cur
                        cur.right = new_node
                        cur = None
                    else:
                        cur = cur.right

        self.size += 1

    def remove(self, value):

        if self.root.value == value:
            new_root = min(self.root.right)
            self.root.value = new_root.value

        elif self.root.value < value:
            self.remove(self.root.right)
        elif self.root.value > value:
            self.remove(self.root.left)

        self.size -= 1

    def search(self, value, node):

        if value == node.value:
            return node

        elif value <= node.value:
            if node.left is not None:
                return self.search(value, node.left)
        elif value > node.value:
            if node.right is not None:
                return self.search(value, node.right)

        return node

    def inorder(self, node):

        if node is None:
            return

        yield self.inorder(node.left)
        yield node
        yield self.inorder(node.right)

    def preorder(self, node):

        pass

    def postorder(self, node):

        pass

    def depth(self, value):

        pass

    def height(self, node):

        if node.parent is None:
            return 0

        return 1 + self.height(self, node.parent)

    def min(self, node):

        if node.left is None:
            return node

        return self.min(node.left)

    def max(self, node):

        if node.right is None:
            return node

        return self.max(node.right)

    def get_size(self):

        return self.size

    def is_perfect(self, node):

        pass

    def is_degenerate(self):

        pass


def main():
    tree = BinarySearchTree()
    print(tree.size)
    print(tree.root)

    tree.insert(2)
    tree.insert(5)
    tree.insert(7)
    tree.insert(7)

    print('Size:')
    print(tree.size)
    print('Values:')
    print(tree.root)
    print(tree.root.right)
    print(tree.root.right.right)


if __name__ == '__main__':
    main()
