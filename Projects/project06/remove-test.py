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

bst.remove(21)
bst.remove(20)
print(bst.root.right.parent)
assert bst.root.right.value == 17

# bst.remove(7)
# assert bst.root.left.left is None
# assert bst.size == 6
#
# bst.remove(13)
# assert bst.root.value == 17
# assert bst.size == 5
#
# bst.remove(10)
# assert bst.root.left.value == 12
# assert bst.size == 4
#
# bst.remove(21)
# bst.remove(20)
# assert bst.size == 2
#
# bst.remove(13)
# assert bst.root.value == 17
# assert bst.size == 2
