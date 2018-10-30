from HashTable import HashTable

ht = HashTable(8)

assert ht.quadratic_probe("abc") == 6
assert ht.quadratic_probe("4") == 4
assert ht.quadratic_probe("b") == 2
assert ht.quadratic_probe("c") == 3
assert ht.quadratic_probe("abcd") == 2