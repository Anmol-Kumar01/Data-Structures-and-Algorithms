class LinkedQueue:
    """FIFO Queue implementation using a singly linked list for storage."""

    class Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def enqueue(self, element):
        """Add element to the rear of the queue (enqueue)."""
        new_node = self.Node(element, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        """
        Remove and return the element from the front of the queue (dequeue).
        Raise Exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return element

    def first(self):
        """
        Return (but do not remove) the element at the front of the queue.
        Raise Exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._head._element

# Example usage:
queue = LinkedQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", len(queue), "elements")  # Output: "Queue: 3 elements"
print("First:", queue.first())  # Output: "First: 1"
print("Dequeue:", queue.dequeue())  # Output: "Dequeue: 1"
print("Queue:", len(queue), "elements")  # Output: "Queue: 2 elements"
