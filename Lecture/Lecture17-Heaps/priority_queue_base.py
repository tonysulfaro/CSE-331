
from exceptions import  Empty

class PriorityQueueBase:
  """Abstract base class for a priority queue."""

  #------------------------------ nested _Item class ------------------------------
  class _Item:
    """Lightweight composite to store priority queue items."""
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
      self._key = k
      self._value = v

    # <editor-fold desc="compare items based on their keys">
    # </editor-fold>
    def __lt__(self, other):
      return self._key < other._key    # compare items based on their keys

    def __repr__(self):
      return '({0},{1})'.format(self._key, self._value)

  #------------------------------ public behaviors ------------------------------

  # <editor-fold desc="Return True if the priority queue is empty">
  # </editor-fold>
  def is_empty(self):                  # concrete method assuming abstract len
    """Return True if the priority queue is empty."""
    return len(self) == 0

  # <editor-fold desc="Return the number of items in the priority queue">
  # </editor-fold>
  def __len__(self):
    """Return the number of items in the priority queue."""
    raise NotImplementedError('must be implemented by subclass')

  # <editor-fold desc="Add a key-value pair">
  # </editor-fold>
  def add(self, key, value):
    """Add a key-value pair."""
    raise NotImplementedError('must be implemented by subclass')

  # <editor-fold desc="Return but do not remove (k,v) tuple with minimum key">#
  # </editor-fold>
  def min(self):
    """Return but do not remove (k,v) tuple with minimum key.

    Raise Empty exception if empty.
    """
    raise NotImplementedError('must be implemented by subclass')

  # <editor-fold desc="Remove and return (k,v) tuple with minimum key.">
  # </editor-fold>
  def remove_min(self):
    """Remove and return (k,v) tuple with minimum key.

    Raise Empty exception if empty.
    """
    raise NotImplementedError('must be implemented by subclass')

