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
        """
        Inserts value into binary tree
        :param value: value to insert into tree
        :return: No Return
        """

        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            cur = self.root
            while cur is not None:
                if new_node.value == cur.value:
                    return
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
        """
        removes element from binary tree if it exists
        :param value: value to search for and delete form tree
        :return: No Return
        """

        # value matches, remove
        if self.root.value == value:

            # left leaf is empty, shift tree
            if self.root.left is None:
                pass
            # right leaf is empty, shift tree
            elif self.root.right is None:
                pass

            # replace root with lesser value in right side of tree
            new_root = self.min(self.root.right)
            self.root.value = new_root.value

        # value is greater than root, search right side
        elif self.root.value < value:
            self.remove(self.root.right)

        # value is lesser than root, search left side
        elif self.root.value > value:
            self.remove(self.root.left)

        self.size -= 1

    def search(self, value, node):
        """
        Searches for a given value with a starting root node
        :param value: value to search for
        :param node: Node from which to complete the search (doesn't have to be the absolute root)
        :return: node - found node or potential parent node if not found
        """

        if value == node.value:
            return node

        elif value < node.value:
            return self.search(value, node.left)

        elif value > node.value:
            return self.search(value, node.right)

        return node

    def inorder(self, node):
        """
        yields inorder traversal of binary tree given starting root
        (Left, Root, Right)
        :param node: root of binary tree to start at
        :return: generator for in order traversal
        """

        if node is None:
            return
        else:
            yield from self.inorder(node.left)
            yield node.value
            yield from self.inorder(node.right)

    def preorder(self, node):
        """
        yeilds preorder traversal of binary tree giving starting root
        (Root, Left, Right)
        :param node: root of binary tree to start at
        :return: generator for in order traversal
        """
        if node is None:
            return
        else:
            yield node.value
            yield from self.preorder(node.left)
            yield from self.preorder(node.right)

    def postorder(self, node):
        """
        yeilds postorder traversal of binary tree giving starting root
        (Left, Right, Root)
        :param node: root of binary tree to start at
        :return: generator for in order traversal
        """
        if node is None:
            return
        else:
            yield from self.postorder(node.left)
            yield from self.postorder(node.right)
            yield node.value

    def depth(self, value):

        node = self.search(value, self.root)
        if node is None:
            return -1

        left_depth = self.height(node.left)
        right_depth = self.height(node.right)

        return 2 + max(left_depth, right_depth)

    def height(self, node):
        """
        Finds height of the tree by counting parents
        :param node: Leaf or body node to start at
        :return: int - height of the tree from node
        """

        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def min(self, node):
        """
        Finds minimum value in binary tree given a starting root node
        :param node: Root Node to start at
        :return: Node - Minimum Node
        """

        if node.left is None:
            return node

        return self.min(node.left)

    def max(self, node):
        """
        Finds maximum value in a binary tree given a starting root node
        :param node: Root Node to start at
        :return: Node - Maximum Node
        """

        if node.right is None:
            return node

        return self.max(node.right)

    def get_size(self):
        """
        Gets size of tree
        :return: int - tree size
        """

        return self.size

    def is_perfect(self, node):

        pass

    def is_degenerate(self):

        pass


def main():
    tree = BinarySearchTree()
    print(tree.size)
    print(tree.root)

    tree.insert(5)
    tree.insert(1)
    tree.insert(4)
    tree.insert(8)
    tree.insert(3)
    tree.insert(2)

    print('Size:')
    print(tree.size)
    print('Root:')
    print(tree.root)

    print('inorder:')
    for value in tree.inorder(tree.root):
        print(value)

    print('preorder:')
    for value in tree.preorder(tree.root):
        print(value)

    print('postorder:')
    for value in tree.postorder(tree.root):
        print(value)


if __name__ == '__main__':
    main()
