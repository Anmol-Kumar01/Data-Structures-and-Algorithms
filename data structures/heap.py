# from priority_base_queue import *
import priority_base_queue
import Empty

class HeapPriorityQueue(priority_base_queue.PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap."""

    ##------------------------------ nonpublic behaviors -----------------------------##

    def _parent(self, j):
    	return (j-1)//2


    def _left(self, j):
    	return 2*j + 1

    def _right(self, j):
    	return 2*j + 2

    def _has_left(self, j):
    	return self._left(j) < len(self._data)

    def _has_right(self, j):
    	return self._left(j) < len(self._data)

    def _swap(self, i, j):

    	self._data[i], self._data[j] = self._data[j], self._data[i]


    def _upheap(self, j):
    	parent = self._parent(j)
    	if j>0 and self._data[j] > self._data[parent]:
    		self._swap(i, parent)
    		self._upheap(parent)
      
      
    def _parent(self, j):
        return (j-1)//2
    
    def _left(self, j):
        return 2*j + 1
    
    def _right(self, j):
        return 2*j + 2
    
    def _has_left(self, j):
        return self._left(j) < len(self._data)
    
    def _has_right(self, j):
        return self._right(j) < len(self._data)
    
    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j>0 and self._data[j] > self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)           # Recursion

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
        if self._has_right(j):
            # right = self._right(j)
            # if self._data[right] > self._data[left]:
            #     small_child = right
            small_child = min(self._right(j), small_child)


        if self._data[small_child] > self._data[j]:
            self._swap(j, small_child)
            self._downheap(small_child)     # Recursion



    ##------------------------------ public behaviors --------------------------------##
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = []

    def is_empty(self):
        """Return True if the priority queue is empty"""
        return len(self._data)==0

    def __len__(self):
        """Return the number of items in the Priority Queue."""
        return len(self)
    
    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data)-1)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.
        
        Raise Empty exception if empty."""
        if self.is_empty():
            raise Empty.EmptyClass("Priority Queue is empty.")
        item = self._data[0]
        return (item._key, item._value)
    
    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.
        
        Raise Empty exception if empty."""
        if self.is_empty():
            raise Empty.EmptyClass("Priority Queue is empty.")
        self._swap(0, len(self._data)-1)                  
        item = self._data.pop()                           # put minimum item at the end
        self._downheap(0)                                 # and remove it from the list;
        return (item._key, item._value)                   # then fix new root
