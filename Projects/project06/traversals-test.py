from BinarySearchTree import BinarySearchTree as stu

bst = stu()

bst.insert(14)
bst.insert(7)
bst.insert(21)
bst.insert(3)
bst.insert(10)
bst.insert(17)
bst.insert(25)

gen1 = bst.preorder(bst.root)
gen2 = bst.postorder(bst.root)
gen3 = bst.inorder(bst.root)

# for i in range(7):
#     print(next(gen1, None))
#     print(next(gen2, None))
#     print(next(gen3, None))
#     print()

pre = [14, 7, 3, 10, 21, 17, 25]
post = [3, 10, 7, 17, 25, 21, 14]
inorder = [3, 7, 10, 14, 17, 21, 25]

for i in range(7):
        print(pre[i])
        a = next(gen1, None)
        print(a)
        print(a, pre[i])
        assert a.value == pre[i]

for i in range(7):
    print(next(gen1, None))
    print(pre[i])
    print()

    print(next(gen2, None))
    print(post[i])
    print()

    print(next(gen3, None))
    print(inorder[i])
    print()

# for i in range(7):
#     assert next(gen1, None) == pre[i]
#     assert next(gen2, None) == post[i]
#     assert next(gen3, None) == inorder[i]
