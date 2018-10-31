from HashTable import string_difference

s1 = "red"
s2 = "blue"

result = string_difference(s1, s2)
expected = set(['r','d','b','l','u'])

assert result == expected

s1 = "green"
s2 = "white"

result = string_difference(s1, s2)
expected = set(['g','r','e','n','h','i','w','t'])

assert result == expected

s1 = "blue"
s2 = "blue"

result = string_difference(s1, s2)
expected = set()

assert result == expected