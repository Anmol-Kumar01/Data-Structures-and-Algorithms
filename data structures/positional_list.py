# from doubly_linked_list import *
import doubly_linked_list


class PositionalList(doubly_linked_list._DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    # Nested Position class representing the location of a single element.
    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            # Constructor should not be invoked by the user.
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element
        
    
        
    def __eq__(self, other):
        """Return True if other is a Position representing the same location."""
        return type(other) is type(self) and other._node is self._node

    def __ne__(self, other):
        """Return True if other does not represent the same location."""
        return not (self == other)  # Opposite of __eq__

    def _validate(self, p):
        """Return the position's node, or raise an appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be a proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:  # Convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return a Position instance for the given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None  # Boundary violation
        else:
            return self.Position(self, node)  # Legitimate position

    def first(self):
        """Return the first Position in the list (or None if the list is empty)."""
        return self.make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if the list is empty)."""
        return self.make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self.validate(p)
        return self.make_position(node._prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self.validate(p)
        return self.make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return a new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return a new Position."""
        return self.insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return a new Position."""
        return self.insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into the list before Position p and return a new Position."""
        original = self.validate(p)
        return self.insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into the list after Position p and return a new Position."""
        original = self.validate(p)
        return self.insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self.validate(p)
        return self.delete_node(original)

    def replace(self, p, e):
        """Replace the element at Position p with e.

        Return the element formerly at Position p.
        """
        original = self.validate(p)
        old_value = original.element  # Temporarily store the old element
        original.element = e  # Replace with the new element
        return old_value  # Return the old element value
if __name__ == '__main__':
    a = PositionalList()
    b = a.add_first(1)
    # print(type(b))
    print(b.element())
    # print(b)
    