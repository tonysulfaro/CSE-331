from BinarySearchTree import BinarySearchTree as stu
from BinarySearchTree import Node
import random as r

bst = stu()
bst.insert(13)
bst.insert(20)
bst.insert(17)
bst.insert(10)
bst.insert(21)
bst.insert(7)
bst.insert(12)

bst.remove(7)

assert bst.root.left.left == None

bst.remove(10)

assert bst.root.left.value == 12

bst.remove(21)
bst.remove(20)

assert bst.root.right.value == 17