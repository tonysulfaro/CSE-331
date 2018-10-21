from BinarySearchTree import BinarySearchTree as stu

bst = stu()

bst.insert(49)
bst.insert(20)
bst.insert(107)
bst.insert(10)
bst.insert(37)
bst.insert(157)
bst.insert(69)

assert bst.min(bst.root).value == 10
assert bst.max(bst.root).value == 157