""" This is the Queue data structure. 
    It is based on FIFO (First In First Out) princippal.
    This has underlying array base implementaion.
    
    Author :  Anmol Kumar
    Date   : 2 September 2023
    
"""
class Queue:
    """ A class used to represent queue data structure.
        Attribute : _data is empty list, used to store the elements of Queue"""
    
    def __init__(self):
        
        self._data = [] # Instanciate the underlying array for queue.
        
    def size(self):
        """Return the size of the queue"""
        return len(self._data)
    
    def enqueue(self, e):
        """ Enqueue(insert) an element in the queue."""
        self._data.append(e)
        
    def dequeue(self):
        """ Remove and Return an element from front of the queue.
        Otherwise raise Error if the queue is empty"""
        if len(self._data) == 0:
            raise Exception(" Queue is empty now")
        else:
            return self._data.pop(0)
    
    def first(self):
        """ Return the element of the queue"""
        return self._data[0]
    
    def is_empty(self):
        """Return True if the queue is empty False otherwise."""
        return self._data == 0
    
    def __len__(self):
        """ Reutrn length of the queue"""
        return(len(self._data))
    
    
    if __name__ == '__main__' :
        print("The Queue data structure is Now exucated ")
        