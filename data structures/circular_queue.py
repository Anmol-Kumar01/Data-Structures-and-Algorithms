class CircularQueue:
    """Queue implementation using a circularly linked list for storage."""

    # Nested Node class for storing a singly linked node.
    class Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # Streamline memory usage

        def __init__(self, element, next):
            # Initialize node's fields
            self._element = element  # Reference to the user's element
            self._next = next        # Reference to the next node

    def __init__(self):
        """Create an empty queue."""
        self._tail = None  # Reference to the tail node (end of the queue)
        self._size = 0    # Number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        head = self._tail._next
        return head._element

    def dequeue(self):
        """Remove and return the first element of the queue (FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        old_head = self._tail._next
        if self._size == 1:  # Removing the only element
            self._tail = None  # Queue becomes empty
        else:
            self._tail._next = old_head._next  # Bypass the old head
        self._size -= 1
        return old_head._element

    def enqueue(self, element):
        """Add an element to the back of the queue."""
        newest = self.Node(element, None)  # Node will be the new tail node
        if self.is_empty():
            newest._next = newest  # Initialize circularly
        else:
            newest._next = self._tail._next  # New node points to the head
            self._tail._next = newest  # Old tail points to the new node
        self._tail = newest  # New node becomes the tail
        self._size += 1

    def rotate(self):
        """Rotate the front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next  # Old head becomes the new tail
