class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    class Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty stack."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, element):
        """Add element to the top of the stack."""
        self._head = self.Node(element, self._head)
        self._size += 1

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._head._element

    def pop(self):
        """
        Remove and return the element from the top of the stack (LIFO).
        Raise Exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        return element

# Example usage:
stack = LinkedStack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", len(stack), "elements")  # Output: "Stack: 3 elements"
print("Top:", stack.top())  # Output: "Top: 3"
print("Pop:", stack.pop())  # Output: "Pop: 3"
print("Stack:", len(stack), "elements")  # Output: "Stack: 2 elements"

