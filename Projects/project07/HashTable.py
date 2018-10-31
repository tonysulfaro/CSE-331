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
        # cannot insert empty string
        if key == '':
            return False

        # check load factor to grow
        if self.size / self.capacity > 0.75:
            self.grow()

        # initialize node and where its going
        new_node = HashNode(key, value)
        bucket = self.quadratic_probe(key)

        if bucket is None:
            return False

        # update existing node value of same key
        if self.table[bucket] is not None and self.table[bucket].key == key:
            self.table[bucket].value = value
            return

        # put new node in
        self.table[bucket] = new_node
        self.size += 1

    def quadratic_probe(self, key):
        """
        finds index of where to insert next item based on key
        :param key: key to search for
        :return: int - index of where to put item in table
        """
        # error handling
        if not key:
            return -1
        if key == '':
            return

        # hash out starting bucket
        bucket = self.hash_function(key) % len(self.table)
        buckets_probed = 0
        while buckets_probed <= len(self.table):
            # if the bucket is empty, the item can be inserted at that index.
            if self.table[bucket] is None:
                return bucket

            # update existing item
            if self.table[bucket].key == key:
                return bucket

            # the bucket was occupied, continue probing to next index in table.
            bucket = (bucket + buckets_probed ** 2) % self.capacity
            buckets_probed = buckets_probed + 1

    def find(self, key):
        """
        find node and return it if it exists, False if DNE
        :param key: key to search map for
        :return: node - if key found, False (bool) - if key not found
        """
        # find hash and start probing there
        bucket = self.hash_function(key) % len(self.table)
        buckets_probed = 0

        # iterate through n elements as worst case
        while buckets_probed < len(self.table):
            # not found
            if self.table[bucket] is None:
                buckets_probed += 1
                continue
            # not in there at all
            if buckets_probed == self.capacity:
                return False
            # found
            if self.table[bucket].key == key:
                return self.table[bucket]

            # the bucket was occupied (now or previously), so continue probing.
            bucket = (bucket + 1) % len(self.table)
            buckets_probed = buckets_probed + 1

        # the entire table was probed or an empty cell was found.
        return False

    def lookup(self, key):
        """
        find key value pair and return value of node
        :param key: key to search for
        :return: value of node
        """
        searched = self.find(key)

        # return value of found node
        if searched is False:
            return searched
        return searched.value

    def delete(self, key):
        """
        remove node from table
        :param key: key to remove from table
        :return: no return
        """
        # error handling
        if not key or key == '':
            return

        bucket = self.hash_function(key) % len(self.table)

        # iterate through n elements as worst case
        buckets_probed = 0
        while buckets_probed < len(self.table):
            # not found
            if self.table[bucket] is None:
                buckets_probed += 1
                continue
            # not in there at all
            if buckets_probed == self.capacity:
                return False
            # found
            if self.table[bucket].key == key:
                self.table[bucket] = None
                self.size -= 1

            # the bucket was occupied (now or previously), so continue probing.
            bucket = (bucket + buckets_probed ** 2) % self.capacity
            buckets_probed = buckets_probed + 1

    def grow(self):
        """
        double table capacity
        :return: no return
        """
        self.table += ([None] * self.capacity)
        self.capacity *= 2
        self.rehash()

    def rehash(self):
        """
        rehashes all items inside the table
        :return: no return
        """
        # initialize temp table
        temp_table = self.table
        self.table = [None] * self.capacity

        # iterate through items and rehash to new positions
        for item in temp_table:
            if item is not None:
                bucket = self.quadratic_probe(item.key)
                self.table[bucket] = item


def string_difference(string1, string2):
    """
    return set difference between two strings using HashTables
    :param string1: first string to compare
    :param string2: second string to compare
    :return: set difference if applicable of strings
    """
    if string2 is None or string1 is None:
        return

    hash_map = HashTable()
    result_set = set()

    # add chars in from string 1
    for char in string1:
        find = hash_map.find(char)
        if find is False:
            hash_map.insert(char, 1)
        else:
            hash_map.insert(find.key, find.value + 1)

    # add in new chars and subtract existing ones to get diff
    for char in string2:
        find = hash_map.find(char)
        if find is False:
            hash_map.insert(char, 1)
        else:
            hash_map.insert(find.key, find.value - 1)

    # get new set and return it
    for item in hash_map.table:
        if item is not None and int(item.value) > 0:
            result_set.add(item.key * int(item.value))

    return result_set


def main():
    """
    main method, not much to see here
    :return: no return
    """
    hashmap = HashTable()
    hashmap.delete(0)
    hashmap.delete(None)
    hashmap.delete('test')
    hashmap.delete('')


if __name__ == '__main__':
    main()
