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
        """
        Insert new key,vale pair into map as a node instance
        :param key: Key of node to insert as
        :param value: Value of node
        :return: Bool - Successful insert or not
        """

        if key == '':
            return False

        if self.size / self.capacity >= 0.75:
            self.grow()

        new_node = HashNode(key, value)
        bucket = self.quadratic_probe(key)

        if bucket is None:
            return False

        if self.table[bucket] is not None and self.table[bucket].key == key:
            self.table[bucket].value = value
            return

        self.table[bucket] = new_node
        self.size += 1

    def quadratic_probe(self, key):

        bucket = self.hash_function(key) % len(self.table)
        buckets_probed = 0
        while buckets_probed <= len(self.table):
            # if the bucket is empty, the item can be inserted at that index.
            if self.table[bucket] is None:
                return bucket

            if self.table[bucket].key == key:
                return bucket

            # the bucket was occupied, continue probing to next index in table.
            bucket = (bucket + buckets_probed ** 2) % len(self.table)
            buckets_probed = buckets_probed + 1

    def find(self, key):
        """
        find node and return it if it exists, False if DNE
        :param key: key to search map for
        :return: node - if key found, False (bool) - if key not found
        """
        bucket = self.hash_function(key) % len(self.table)
        buckets_probed = 0
        while buckets_probed < len(self.table):
            if self.table[bucket] is None:
                buckets_probed += 1
                continue
            if buckets_probed == self.capacity:
                return False
            if self.table[bucket].key == key:
                return self.table[bucket]

            # the bucket was occupied (now or previously), so continue probing.
            bucket = (bucket + 1) % len(self.table)
            buckets_probed = buckets_probed + 1

        # the entire table was probed or an empty cell was found.
        return False

    def lookup(self, key):
        searched = self.find(key)

        if searched is False:
            return searched
        return searched.value

    def delete(self, key):
        pass

    def grow(self):

        temp_table = [None] * (self.capacity * 2)

        for item in self.table:
            if item is not None:
                bucket = self.quadratic_probe(item.key)
                temp_table[bucket] = item

        self.table = temp_table

    def rehash(self):
        pass


def string_difference(string1, string2):
    pass


def main():
    table = HashTable(10)
    table.insert('tony', 20)
    table.insert('jim bob', 30)
    table.insert('tony', 50)
    print(table.size)

    print(table.find('tony'))
    print(table.find('not found'))


if __name__ == '__main__':
    main()
