from priority_queue_base import PriorityQueueBase
from positional_list import PositionalList
from exceptions import Empty


class UnsortedPriorityQueue(PriorityQueueBase):  # base class defines _Item
    """A min-oriented priority queue implemented with an unsorted list."""

    # ----------------------------- nonpublic behavior -----------------------------
    def _find_min(self):
        """Return Position of item with minimum key."""
        pass
    # ------------------------------ public behaviors ------------------------------
    def __init__(self):
        """Create a new empty Priority Queue."""
        pass

    def __len__(self):
        """Return the number of items in the priority queue."""
        pass

    def add(self, key, value):
        """Add a key-value pair."""
        pass

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.
    
        Raise Empty exception if empty.
        """
        pass
    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.
    
        Raise Empty exception if empty.
        """
        pass






# test
pqueu = UnsortedPriorityQueue()
pqueu.add(5, 'A')
pqueu.add(9, 'C')
pqueu.add(3, 'B')
print(str(pqueu.min()))
pqueu.remove_min()
print(str(pqueu.min()))


