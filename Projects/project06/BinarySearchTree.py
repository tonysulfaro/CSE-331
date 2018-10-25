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
            while cur is not None:  # iterate through to find where to put new node
                if new_node.value == cur.value:
                    return
                if new_node.value < cur.value:  # search left side of tree to insert
                    if cur.left is None:
                        # set new node attributes
                        new_node.parent = cur
                        cur.left = new_node
                        cur = None
                    else:
                        cur = cur.left  # keep searching right side
                else:  # search right side of tree to insert
                    if cur.right is None:
                        # set new node attributes
                        new_node.parent = cur
                        cur.right = new_node
                        cur = None
                    else:
                        cur = cur.right  # keep searching right side

        self.size += 1

    def remove(self, value):
        """
        removes element from binary tree if it exists
        :param value: value to search for and delete form tree
        :return: No Return
        """

        if self.root is None:
            return

        par = None
        cur = self.root
        while cur is not None:  # iterate through tree
            if cur.value == value:  # found matching node
                if not cur.left and not cur.right:  # remove leaf
                    if not par:  # node is root
                        self.root = None
                    elif par.left == cur:
                        par.left = None
                    else:
                        par.right = None

                elif cur.left and not cur.right:  # remove one left child
                    if not par:  # node is root:
                        self.root = cur.left
                        cur.left.parent = None
                    elif par.left == cur:
                        par.left = cur.left
                        cur.left.parent = par
                    else:
                        par.right = cur.left
                        cur.left.parent = par

                elif not cur.left and cur.right:  # Remove node with only right child
                    if not par:  # node is root
                        self.root = cur.right
                        cur.right.parent = None
                    elif par.left == cur:
                        par.left = cur.right
                        cur.right.parent = par
                    else:
                        par.right = cur.right
                        cur.right.parent = par

                else:  # Remove node with two children
                    # Find successor (leftmost child of right subtree)
                    suc = self.min(cur.right)
                    self.remove(suc.value)

                    self.size += 1

                    successorData = Node(suc.value, None)
                    successorData.left = cur.left
                    successorData.right = cur.right
                    successorData.parent = par

                    # Assign children of new node to new parent
                    if successorData.left is not None:
                        successorData.left.parent = successorData
                    if successorData.right is not None:
                        successorData.right.parent = successorData

                    # Assign cur's data with successorData
                    if cur.parent is not None:
                        if cur.parent.left == cur:
                            cur.parent.left = successorData
                        if cur.parent.right == cur:
                            cur.parent.right = successorData
                    cur = successorData

                    if cur.parent is None:
                        self.root = successorData

                self.size -= 1
                return  # Node found and removed

            elif cur.value < value:  # Search right
                par = cur
                cur = cur.right

            else:  # Search left
                par = cur
                cur = cur.left

        return  # Node not found

    def search(self, value, node):
        """
        Searches for a given value with a starting root node
        :param value: value to search for
        :param node: Node from which to complete the search (doesn't have to be the absolute root)
        :return: node - found node or potential parent node if not found
        """

        # match or invalid node
        if node is None or node.value == value:
            return node

        # search left if value is lesser
        if value < node.value:
            if node.left is None:
                return node
            else:
                return self.search(value, node.left)

        # search right if value is greater
        elif value > node.value:
            if node.right is None:
                return node
            else:
                return self.search(value, node.right)

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
        """
        get depth of tree from root to value by iterating through the tree
        :param value: value to search for
        :return: int - depth of value relative to root, -1 if not found
        """

        count = 0
        cur = self.root
        # essentially search but count how many times you move down a level
        while cur is not None:
            if cur.value == value:
                return count
            if cur.value < value:
                cur = cur.right
                count += 1
            elif cur.value > value:
                cur = cur.left
                count += 1
        return -1

    def height(self, node):
        """
        Finds height of the tree by counting parents
        :param node: Leaf or body node to start at
        :return: int - height of the tree from node
        """

        if node is None:
            return -1

        # search both sides of tree to find just how big it is
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def min(self, node):
        """
        Finds minimum value in binary tree given a starting root node
        :param node: Root Node to start at
        :return: Node - Minimum Node
        """

        # just keep going left until you cant go anymore
        if node is None or node.left is None:
            return node
        else:
            return self.min(node.left)

    def max(self, node):
        """
        Finds maximum value in a binary tree given a starting root node
        :param node: Root Node to start at
        :return: Node - Maximum Node
        """

        # just keep going right until you cant go anymore
        if node is None or node.right is None:
            return node
        else:
            return self.max(node.right)

    def get_size(self):
        """
        Gets size of tree
        :return: int - tree size
        """

        return self.size

    def is_perfect(self, node):
        """
        bool for if tree is perfect or not (size == (2^h)-1)
        :param node: root node to start at
        :return: bool - is_perfect or not
        """

        # empty tree
        if node is None:
            return True

        # only one element in tree
        if node is not None and node.left is None and node.right is None:
            return True

        # fully loaded tree
        if self.size == 2 ** (self.height(self.root) + 1) - 1:
            return True

        return False

    def is_degenerate(self):
        """
        returns if tree is basically a linked list (all nodes have only one child)
        :return: bool, if is degenerate
        """

        if self.is_perfect(self.root):
            return False
        # degenerate if number of elements is height + 1
        return self.size == self.height(self.root) + 1
