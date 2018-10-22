from BinarySearchTree import BinarySearchTree as stu

bst = stu()

bst.insert(40)
bst.insert(20)
bst.insert(60)
bst.insert(10)
bst.insert(30)
bst.insert(50)
bst.insert(70)

print(bst.search(25, bst.root.left))
assert bst.search(5, bst.root.left) == bst.root.left.left
assert bst.search(75, bst.root) == bst.root.right.right
assert bst.search(25, bst.root) == bst.root.left.right
