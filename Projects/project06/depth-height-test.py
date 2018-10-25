from BinarySearchTree import BinarySearchTree as stu

bst = stu()

bst.insert(21)
bst.insert(10)
bst.insert(32)
bst.insert(5)
bst.insert(16)
bst.insert(27)
bst.insert(39)

# print(bst.depth(5))
# print(bst.depth(10))
# print(bst.height(bst.root))
# print(bst.height(bst.root.left))

assert bst.depth(5) == 2
assert bst.depth(10) == 1

assert bst.height(bst.root) == 2
assert bst.height(bst.root.left) == 1

tree = stu()

assert tree.height(tree.root) == -1

tree.insert(1)
#print(tree.height(tree.root))
print(tree.depth(1))
tree.insert(2)
#print(tree.height(tree.root))
tree.insert(3)
#print(tree.height(tree.root))
tree.insert(4)
tree.insert(5)

#print(tree.height(tree.root))
print(tree.depth(tree.root.value))
print(tree.depth(3))
print(tree.depth(6))
print(tree.height(tree.root))