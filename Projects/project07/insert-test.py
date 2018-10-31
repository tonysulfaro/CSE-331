from HashTable import HashTable


def assertNode(node, key, value):
    if key is None:
        assert node is None
    else:
        assert node.key == key and node.value == value


ht = HashTable()

ht.insert("abc", 1)
ht.insert("acb", 2)
ht.insert("bac", 3)

assertNode(ht.table[0], "bac", 3)
assertNode(ht.table[1], None, None)
assertNode(ht.table[2], "abc", 1)
assertNode(ht.table[3], "acb", 2)

ht.insert("abc", 10)  # Reassignment

assertNode(ht.table[2], "abc", 10)

assert ht.size == 3
assert ht.capacity == 4
