from BinarySearchTree import BinarySearchTree as stu

bst = stu()

assert bst.is_perfect(bst.root) == True
assert bst.is_degenerate() == False

for i in range(10):
    bst.insert(i)

assert bst.is_degenerate() == True
assert bst.is_perfect(bst.root) == False

bst = stu()

bst.insert(10)
bst.insert(8)
bst.insert(12)
bst.insert(7)
bst.insert(9)
bst.insert(11)

assert bst.is_degenerate() == False
assert bst.is_perfect(bst.root) == False

bst.insert(13)

assert bst.is_degenerate() == False

print(bst.height(bst.root)+1)
print(2**(bst.height(bst.root)+1)-1)
assert bst.is_perfect(bst.root) == True