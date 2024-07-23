class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'  # Streamline memory

        def __init__(self, element, prev, next):
            # Initialize node's fields
            self._element = element  # User's element
            self._prev = prev        # Previous node reference
            self._next = next        # Next node reference

    def __init__(self):
        """Create an empty list."""
        self._header = self.Node(None, None, None)
        self._trailer = self.Node(None, None, None)
        self._header._next = self._trailer  # Trailer is after the header
        self._trailer._prev = self._header  # Header is before the trailer
        self._size = 0  # Number of elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return the new node."""
        newest = self.Node(e, predecessor, successor)  # Linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete a nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1  
        element = node._element  # Record deleted element
        node._prev = node._next = node._element = None  # Deprecate node
        return element  # Return deleted element
