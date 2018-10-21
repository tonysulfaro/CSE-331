from BinarySearchTree import BinarySearchTree as stu


bst = stu()

bst.insert(40)
bst.insert(20)
bst.insert(60)
bst.insert(10)
bst.insert(30)
bst.insert(50)
bst.insert(70)

thing = bst.search(20, bst.root)
non_exist = bst.search(25, bst.root)

assert 20 == bst.root.left.value
assert 70 == bst.root.right.right.value
#assert 25 == bst.root.left.right.value

assert bst.search(20, bst.root) == bst.root.left
assert bst.search(70, bst.root) == bst.root.right.right
assert bst.search(25, bst.root) == bst.root.left.right
