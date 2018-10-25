
from .hash_map_base import HashMapBase
from .unsorted_table_map import UnsortedTableMap

class ChainHashMap(HashMapBase):
  """Hash map implemented with separate chaining for collision resolution."""

  def _bucket_getitem(self, j, k):
    bucket = self._table[j]
    if bucket is None:
      raise KeyError('Key Error: ' + repr(k))        # no match found
    return bucket[k]                                 # may raise KeyError

  def _bucket_setitem(self, j, k, v):
    if self._table[j] is None:
      self._table[j] = UnsortedTableMap()     # bucket is new to the table
    oldsize = len(self._table[j])
    self._table[j][k] = v
    if len(self._table[j]) > oldsize:         # key was new to the table
      self._n += 1                            # increase overall map size

  def _bucket_delitem(self, j, k):
    bucket = self._table[j]
    if bucket is None:
      raise KeyError('Key Error: ' + repr(k))        # no match found
    del bucket[k]                                    # may raise KeyError

  def __iter__(self):
    for bucket in self._table:
      if bucket is not None:                         # a nonempty slot
        for key in bucket:
          yield key



chainhash=ChainHashMap()
chainhash.__setitem__("A",10)
chainhash.__setitem__("B",20)
chainhash.__setitem__("A",200)
chainhash.__setitem__("C",35)
chainhash.__setitem__("Z",13)
chainhash.__setitem__("D",21)
chainhash.__setitem__("G",100)
chainhash.__setitem__("W",1)
chainhash.__delitem__("B")



