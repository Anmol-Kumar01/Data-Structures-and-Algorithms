from postional_list import *
from binary_tree import *

class LinkedBinaryTree(Binary.Tree):
    
    class _Node:
        
        __slots__ = "_element", "_parent", "_left", "_right"
        def __init__(self, element, parent = None, left = None, right = None):
        
        
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right 
            
        
        class Position(Binary.Postion):
            
            def __init__(self, container, node):
                
                self._container = container
                self._node = node
                
            
            def element(self):
                
                return self._node._element
                
            def __eq__(self, other):
                
                return type(other) == type(self) and other._node == self._node
            
        
        def _validate(self, p):
            if not isinstance(p, self.Position):
                raise TypeError("p must be a proper Position type")
            
            if p._container is not self:
                raise ValueError("p does not belong to this container")
            
            if p._node._parent is p._node:
                raise ValueError("p is no longer valid")
            
            return p._node
        
        
        def _make_position(sefl, node):
            
            if node != None:
                return self.Position(self, node)
            else:
                return None
        
#---------------------------------------------------------- binary tree constructor --------------------------------------------------#

        
        def __init__(self):
            
            self._root = None
            self._size = 0
            
#--------------------------------------------------------- public accessors -----------------------------------------------------------#

        def __len__(self):
            return self._size
        
        def root (Self):
            return self._make_position(self._root)
        
        
        def parent(self, parent):
        
            node = self._validate(p)
            return self._make_position(node._parent)
        
        def left(self, p):
            
            node = self._validate(p)
            return self._make_position( node._left)
        
        def right(self, p):
            
            node = self._validate(p)
            return self._make_position( node._right)
        
        
        def num_children( self, p):
            
            node = self._validate(p)
            count = 0
            if node._left is not None:
                count +=1
            if node._right is not None:
                count +=1
            return count
        
        
        def _add_root(self, eelement):
            
            if self._root != None:
                raise ValueError(" Root already exits")
            self._size = 1
            self._root = self._Node(element)
            return self._make_position(self._root)
            
        
        def _add_left(self, p, element):
            
            node = self._validate(p)
            
            if node._left is not None:
                raise ValueError(" Left child already exists")
            self._size +=1
            self._left = self._Node(element, node)
            
            return self._make_position(self._left)
            
            
        def _add_rightt(self, p, element):
            
            node = self._validate(p)
            
            if node._right is not None:
                raise ValueError(" Right child already exists")
            self._size +=1
            self._right = self._Node(element, node)
            
            return self._make_position(self._right)
        
        def _replace(self, p, elemnt):
            
            node = self._validate(p)
            old_element = node._element 
            node._element = element
            
            return old_element
        
        def _delete(self, p):
            
            node = self._validate(p)
            if self.num_children(p) == 2:
                raise ValueError(" p has two children")
            child = node._left if node._left else node._right
            
            if child is not None:
                child._parent = node._parent
                
            if node is self._root:
                self._root = child
            
            else:
                parent = child._parent
                if child is parent._left:
                    parent._left = child
                else:
                    parent._right = child
                
            self._size -=1
            
            node._parent = node
            return node._element
        
        
        def _attach(self, p, t1, t2):
            
            node = self._validate(p)
            if not self.is_leaf:
                raise ValueError("Position must be leaf")
            if not type(self) is type(t1) is type(2):
                raise TypeError("Trees types must be same")
            self._size = self._size + len(t1) + len(t2)
            
            if not t1.is_empty():
                t1._root._parent = node
                node._left = t1._root
                t1.root = None
                t1._size = 0
                
            if not t2.is_empty():
                t2._root._parent = node
                node._right = t2._root
                t2.root = None
                t2._size = 0
                
                
#------------------------------------ Tree Traversals -----------------------------------#
    #------------------Preorder Traversal-------------------------#
       
       
        def _subtree_preorder(self, p):
            
            yield p
            for c in self.children(p):
                for other in self._subtree_preorder(c):
                    yield other 
        
        
        def preorder( T, p):
            
            if not self.is_empty():
                for p in self.__subtree_preorder(self.root()):
                    yield p
                    
        
        def positions(self):
            
            return self.preorder()
                    
    #---------------------Post Traversal--------------------------#

        
        def _subtree_postorder(self, p):
            
            for c in self.children(p):
                for other in self._subtree_postorder(c):
                    yield other 
            yield p 
    
        
        def postorder(self):
            
            if not self.is_empty():
                for p in self._subtree_postorder(self.root()):
                    yield p
                    
                    
    #-------------------Breadth First Search---------------------#
    
        def breadthfirst(self):
            
            if not self.is_empty():
                
                fringe = LinkedQueue()
                fringe.enqueue(self.root())
                
                while not fringe.is_empty():
                    
                    p = fringe.dequeue()
                    yield p
                    
                    for c in self.children(p):
                        fringe.enqueue(c)
                        
    #--------------------Inorder Traversal----------------------#
    
        def _subtree_inorder(self, p):
            
            if self.left(p) is not None:
                for other in self._subtree_inorder(self.left(p)):
                    yield other
                    
            yield p
            
            if self.right(p) is not None:
                for other in self._subtree_inorder(self.right(p)):
                    yield other 
                    
        
        def inorder(self):
            
            if not self.is_empty():
                for p in self._subtree_inorder(self.root()):
                    yield p
                    
                    
    
        
                
        
        
    
    
                    
            