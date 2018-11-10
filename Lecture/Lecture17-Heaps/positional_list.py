
from doubly_linked_base import _DoublyLinkedBase
class PositionalList(_DoublyLinkedBase):
  """A sequential container of elements allowing positional access."""
  #-------------------------- nested Position class --------------------------
  class Position:
    """An abstraction representing the location of a single element.

    Note that two position instaces may represent the same inherent
    location in the list.  Therefore, users should always rely on
    syntax 'p == q' rather than 'p is q' when testing equivalence of
    positions.
    """

    # <editor-fold desc="Constructor should not be invoked by user">
    # </editor-fold>
    def __init__(self, container, node):
      """Constructor should not be invoked by user."""
      self._container = container
      self._node = node

    # <editor-fold desc="Return the element stored at this Position">
    # </editor-fold>
    def element(self):
      """Return the element stored at this Position."""
      return self._node._element

    # <editor-fold desc="Return True if other is a Position representing the same location">
    # </editor-fold>
    def __eq__(self, other):
      """Return True if other is a Position representing the same location."""
      return type(other) is type(self) and other._node is self._node

    # <editor-fold desc="Return True if other does not represent the same location">
    # </editor-fold>
    def __ne__(self, other):
      """Return True if other does not represent the same location."""
      return not (self == other)               # opposite of __eq__

  #------------------------------- utility methods -------------------------------
  # <editor-fold desc="Return position's node, or raise appropriate error if invalid">
  # </editor-fold>
  def _validate(self, p):
    """Return position's node, or raise appropriate error if invalid."""
    if not isinstance(p, self.Position):
      raise TypeError('p must be proper Position type')
    if p._container is not self:
      raise ValueError('p does not belong to this container')
    if p._node._next is None:                  # convention for deprecated nodes
      raise ValueError('p is no longer valid')
    return p._node

  # <editor-fold desc="Return Position instance for given node (or None if sentinel)."
  # </editor-fold>
  def _make_position(self, node):
    """Return Position instance for given node (or None if sentinel)."""
    if node is self._header or node is self._trailer:
      return None  # boundary violation
    else:
      return self.Position(self, node)  # legitimate position
  #------------------------------- accessors -------------------------------
  # <editor-fold desc="Return the first Position in the list (or None if list is empty)">
  # </editor-fold>
  def first(self):
    """Return the first Position in the list (or None if list is empty)."""
    return self._make_position(self._header._next)

  # <editor-fold desc="Return the last Position in the list (or None if list is empty).">
  # </editor-fold>
  def last(self):
    """Return the last Position in the list (or None if list is empty)."""
    return self._make_position(self._trailer._prev)

  # <editor-fold desc="Return the Position just before Position p (or None if p is first)">
  # </editor-fold>
  def before(self, p):
    """Return the Position just before Position p (or None if p is first)."""

    node = self._validate(p)
    return self._make_position(node._prev)

  # <editor-fold desc="Return the Position just after Position p (or None if p is last)">
  # </editor-fold>
  def after(self, p):
    """Return the Position just after Position p (or None if p is last)."""
    node = self._validate(p)
    return self._make_position(node._next)

  # <editor-fold desc="Generate a forward iteration of the elements of the list"
  # </editor-fold>
  def __iter__(self):
    """Generate a forward iteration of the elements of the list."""
    cursor = self.first()
    while cursor is not None:
      yield cursor.element()
      cursor = self.after(cursor)

  #------------------------------- mutators -------------------------------
  # override inherited version to return Position, rather than Node

  # <editor-fold desc="Add element between existing nodes and return new Position">
  # </editor-fold>
  def _insert_between(self, e, predecessor, successor):
    """Add element between existing nodes and return new Position."""
    node = super()._insert_between(e, predecessor, successor)
    return self._make_position(node)

  # <editor-fold desc="Insert element e at the front of the list and return new Position.">
  # </editor-fold>
  def add_first(self, e):
    """Insert element e at the front of the list and return new Position."""
    return self._insert_between(e, self._header, self._header._next)

  # <editor-fold desc="Insert element e at the back of the list and return new Position">
  # </editor-fold>
  def add_last(self, e):
    """Insert element e at the back of the list and return new Position."""
    return self._insert_between(e, self._trailer._prev, self._trailer)

  # <editor-fold desc="Insert element e into list before Position p and return new Position">
  # </editor-fold>
  def add_before(self, p, e):
    """Insert element e into list before Position p and return new Position."""
    original = self._validate(p)
    return self._insert_between(e, original._prev, original)

  # <editor-fold desc="Insert element e into list after Position p and return new Position">
  # </editor-fold>
  def add_after(self, p, e):
    """Insert element e into list after Position p and return new Position."""
    original = self._validate(p)
    return self._insert_between(e, original, original._next)

  # <editor-fold desc="Remove and return the element at Position">
  # </editor-fold>
  def delete(self, p):
    """Remove and return the element at Position p."""
    original = self._validate(p)
    return self._delete_node(original)  # inherited method returns element
  # <editor-fold desc="Replace the element at Position p with e.Return the element formerly at Position p">
  # </editor-fold>
  def replace(self, p, e):
    """Replace the element at Position p with e.

    Return the element formerly at Position p.
    """
    original = self._validate(p)
    old_value = original._element       # temporarily store old element
    original._element = e               # replace with new element
    return old_value                    # return the old element value




