from HashTable import HashTable


def assertNode(node, key, value):
    if key is None:
        assert node is None or node is False
    else:
        assert node.key == key and node.value == value


ht = HashTable(8)

ht.insert("abc", 1)
ht.insert("word", 2)
ht.insert("test", 3)
ht.insert("bean", 4)
ht.insert("five", 5)

ht.delete("abc")
ht.delete("test")
ht.delete("five")
ht.delete(None)
ht.delete(0)

assertNode(ht.table[0], "word", 2)
assertNode(ht.table[1], None, None)
assertNode(ht.table[2], "bean", 4)
for i in range(3, 8):
    assertNode(ht.table[i], None, None)
