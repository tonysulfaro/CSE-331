from BinarySearchTree import BinarySearchTree as stu

bst = stu()

bst.insert(40)
bst.insert(20)
bst.insert(60)
bst.insert(10)
bst.insert(30)
bst.insert(50)
bst.insert(70)

assert bst.search(40, bst.root) == bst.root
assert bst.search(20, bst.root) == bst.root.left
assert bst.search(10, bst.root) == bst.root.left.left
assert bst.search(30, bst.root) == bst.root.left.right

assert bst.search(60, bst.root) == bst.root.right
assert bst.search(50, bst.root) == bst.root.right.left
assert bst.search(70, bst.root) == bst.root.right.right

parent = bst.search(5, bst.root)
assert bst.search(5, bst.root) == bst.root.left.left
assert bst.search(75, bst.root) == bst.root.right.right
assert bst.search(25, bst.root) == bst.root.left.right

bst.remove(40)
print(bst.search(40, bst.root))
print(bst.root.left)
assert bst.search(40, bst.root) == bst.root.left.right
#assert bst.search(25, bst.root) == bst.root
