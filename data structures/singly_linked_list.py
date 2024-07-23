class Node:
    def __init__(self, element, next=None):
        """Initialize a Node with an element and an optional reference to the next node."""
        self._element = element
        self._next = next

class Linked_list:
    def __init__(self):
        """Initialize an empty linked list with no head node and size 0."""
        self._head = None  # Head of the linked list
        self._size = 0    # Size of the linked list
        
    def add_first(self, element):
        """Add an element to the front (head) of the linked list."""
        # Create a new node with the given element and set its next reference to the current head
        node = Node(element, self._head)
        self._head = node  # Update the head to the new node
        self._size += 1    # Increment the size of the linked list

    def add_last(self, element):
        """Add an element to the end (tail) of the linked list."""
        if self._head is None:
            # If the list is empty, create a new node and set it as the head
            self._head = Node(element, None)
        else:
            # Traverse to the end of the list and add a new node there
            iter = self._head
            while iter._next:
                iter = iter._next
            iter._next = Node(element, None)
        self._size += 1

    def remove_first(self):
        """Remove and return the first element from the linked list."""
        if self._head is None:
            raise Exception("Linked List is Empty")
        element = self._head._element
        self._head = self._head._next  # Update the head to the next node
        self._size -= 1
        return element

    def __len__(self):
        """Return the size (number of elements) of the linked list."""
        return self._size

    def __str__(self):
        """Return a string representation of the linked list."""
        curr_node = self._head
        result = ""
        while curr_node is not None:
            result += str(curr_node._element) + "-->"
            curr_node = curr_node._next
        return result

    def remove_last(self):
        """Remove and return the last element from the linked list."""
        if self._size == 0:
            raise Exception("Linked List is Empty")
        if self._head._next is None:
            # If there's only one element, remove it and set the head to None
            element = self._head._element
            self._head = None
            self._size -= 1
            return element
        else:
            iter = self._head
            while iter._next._next:
                iter = iter._next
            element = iter._next._element
            iter._next = None
            self._size -= 1
            return element
    
    

# Example usage:
l = Linked_list()
l.add_first(3)
l.add_first(4)
print(l)

    