from priority_queue_base import PriorityQueueBase
from positional_list import PositionalList
from exceptions import Empty


class SortedPriorityQueue(PriorityQueueBase):  # base class defines _Item
    """A min-oriented priority queue implemented with a sorted list."""

    # ------------------------------ public behaviors ------------------------------
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        newest = self._Item(key, value)
        walk = self._data.last()  # walk backward look for smaller

        while walk and newest < walk.element():
            walk = self._data.before(walk)

        if not walk:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        first = self._data.first()
        item = first.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        min = self._data.first()
        item = self._data.delete(min)
        return (item._key, item._value)


# test
pqueu = SortedPriorityQueue()
pqueu.add(5, 'A')
pqueu.add(9, 'C')
pqueu.add(3, 'B')
print(str(pqueu.min()))
pqueu.remove_min()
print(str(pqueu.min()))
