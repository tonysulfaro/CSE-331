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
assert bst.size == 7

bst.remove(20)
print(bst.root)

tree = stu()
tree.insert(5)
#tree.remove(5)
print(tree.root)
print(tree.depth(tree.root))