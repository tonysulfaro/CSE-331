from HashTable import HashTable


def assertNode(node, key, value):
    if key is None:
        assert node is None
    else:
        assert node.key == key and node.value == value


ht = HashTable(8)

ht.insert("abc", 1)
ht.insert("acb", 2)
ht.insert("bac", 3)
ht.insert("hello", 4)
ht.insert("wasd", 5)

n1 = ht.find("abc")
n2 = ht.find("acb")
n3 = ht.find("bac")
n4 = ht.find("hello")
n5 = ht.find("wasd")

assertNode(n1, "abc", 1)
assertNode(n2, "acb", 2)
assertNode(n3, "bac", 3)
assertNode(n4, "hello", 4)
assertNode(n5, "wasd", 5)

assert ht.find("Not Real") == False