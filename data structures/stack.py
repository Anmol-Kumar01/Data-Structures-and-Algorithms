"""Stack is based on LIFO (Last In First Out) principal data structure. 
   This the stack data structure implementation based on unlying array.
   We will use this for implementing different functions.
    
    Author : Anmol Kumar
    Date   : 2 September 2023
"""

class Stack:
    """ A class used to represent Stack data structure.
        Attribute : _data is empty list, used to store the elements of stack
    """
    
    def __init__(self):
        """ Intialize an empty list that will
        used to store the elements of stack.
        """
        self._data = [] # instanciating the underlying array for stack

    def push(self, a):
        """ Insert an element in the stack."""
        self._data.append(a) # Inserting a element into a stack
    

    def is_empty(self):
        """Return True if the stack is empty or False otherwise."""
        return len(self._data) == 0  

    def top(self):
        """ Return the top most element of the stack
        (element which has been latest pushed) 
        or raised Error otherwise"""
        if self.is_empty():
            raise Exception("Stack has No Elements")
        else:
            return self._data[-1]

    def pop(self):
        """ Remove and Return the last element of the stack
        raise Error if the stack is empty"""
        if self.is_empty():
            raise Exception("Stack has no Elements")
        else:
            return self._data.pop()

    def __len__(self):
        """Return the length of the stack"""
        return(len(self._data))

    if __name__ == '__main__' :
        print("The Stack data structure is being exucated ")
        s = Stack()
        s.push(5)
        print(len(s))

