from HashTable import HashTable


def assertNode(node, key, value):
    if key is None:
        assert node is None
    else:
        assert node.key == key and node.value == value


ht = HashTable()

for i in range(6):
    ht.insert(i * 'a', i)

assert ht.size == 5
assert ht.capacity == 8

assertNode(ht.table[0], None, None)
assertNode(ht.table[1], 'a', 1)
assertNode(ht.table[2], None, None)
assertNode(ht.table[3], None, None)
assertNode(ht.table[4], "aaaa", 4)
assertNode(ht.table[5], "aaaaa", 5)
assertNode(ht.table[6], "aa", 2)
assertNode(ht.table[7], "aaa", 3)
