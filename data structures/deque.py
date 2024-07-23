# import queue
""" The Deque Abstract Data Type.  
    It gives us flexibility that we can add or delete from both ends of the deque.
"""

class Deque:
    """A class that represents Double Ended Queue
       It is a special type of queue that give flexibility to add or delete
       from the both ends.""" 
       
    def __init__(self):
        """ Initialize the underlyling array for deque"""
        self._data = []
        
    def add_first(self, element):
        """ Insert element at first index of the queue"""
        if self.is_empty():
            self._data.append(element)
        else:
            self._data.insert(0, element)
        
    def add_last(self, element):
        """ Insert element at the last index of the queue"""
        self._data.append(element)
        
    def delete_first(self):
        """ Remove and return the first element of the deque or raise error if deque is empty"""
        if self.is_empty():
            raise Exception("Double ended queue is empty")
        else:
            return self._data.pop(0)
            
    def delete_last(self):
        """ Remove and return the last element of the deque or raise error if deque is empty"""
        if self.is_empty():
            raise Exception("Double ended queue is empty")
        else:
            return self._data.pop()
            
    def first(self):
        """Return the first element of the deque"""
        return self._data[0]
    
    def last(self):
        """ Return the last element of the deque"""
        if self.is_empty():
            raise Exception("Dwouble ended queue is empty")
        else: 
            return self._data[len(self._data)-1]
    
    def is_empty(self):
        """ Return True if deque is empty False otherwise."""
        return len(self._data) == 0
    
    def __len__(self):
        """ Return the length of the deque"""
        return(len(self._data))
        
        
    
        