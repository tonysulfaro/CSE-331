class HashNode:
    """
    DO NOT EDIT
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"


class HashTable:
    """
    Hash table class, utilizes double hashing for conflicts
    """

    def __init__(self, capacity=4):
        """
        DO NOT EDIT
        Initializes hash table
        :param tableSize: size of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        pass

    def hash_function(self, x):
        """
        ---DO NOT EDIT---

        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not x:
            return -1
        hashed_value = 0

        for char in x:
            hashed_value = 181 * hashed_value + ord(char)

        return hashed_value % self.capacity

    def insert(self, key, value):
        pass

    def quadratic_probe(self, key):
        pass

    def find(self, key):
        pass

    def lookup(self, key):
        pass

    def delete(self, key):
        pass

    def grow(self):
        pass

    def rehash(self):
        pass


def string_difference(string1, string2):
    pass
