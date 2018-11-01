from priority_queue_base import PriorityQueueBase
from exceptions import Empty


class HeapPriorityQueue(PriorityQueueBase):  # base class defines _Item
    """A min-oriented priority queue implemented with a binary heap."""

    # ------------------------------ nonpublic behaviors ------------------------------

    def _parent(self, j):
        # find parent index
        pass

    def _left(self, j):
        # find left index
        pass

    def _right(self, j):
        # find right index
        pass

    def _has_left(self, j):
        return self._left(j) < len(self._data)  # index beyond end of list?

    def _has_right(self, j):
        return self._right(j) < len(self._data)  # index beyond end of list?

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        pass

    def _downheap(self, j):
        pass

    # ------------------------------ public behaviors ------------------------------
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = []

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        # self._data.append(self._Item(key, value))
        pass  # upheap newly added position

    # <editor-fold desc="Return but do not remove (k,v) tuple with minimum key">
    # </editor-fold>
    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data[0]
        return (item._key, item._value)

    # <editor-fold desc="Remove and return (k,v) tuple with minimum key.Raise Empty exception if empty">
    # </editor-fold>
    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
            # put minimum item at the end
            # and remove it from the list;
            # then fix new root


pqueu = HeapPriorityQueue()
pqueu.add(5, 'A')
pqueu.add(4, 'B')
pqueu.add(3, 'B')
pqueu.add(9, 'C')
pqueu.add(3, 'B')
pqueu.add(1, 'A')

print(str(pqueu.min()))
pqueu.remove_min()
print(str(pqueu.min()))
