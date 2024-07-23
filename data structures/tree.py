
class Tree:
    """Abstract base class representing a tree structure."""

    # ----------------------- Nested Position class -----------------------

    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError("Must be implemented by a subclass.")

        def eq(self, other):
            """Return True if the other Position represents the same location."""
            raise NotImplementedError("Must be implemented by a subclass.")

        def ne(self, other):
            """Return True if the other does not represent the same location."""
            return not (self == other)  # Opposite of eq

        # Abstract methods that concrete subclasses must support

        def root(self):
            """Return Position representing the tree's root (or None if empty)."""
            raise NotImplementedError("Must be implemented by a subclass.")

        def parent(self, p):
            """Return Position representing p's parent (or None if p is the root)."""
            raise NotImplementedError("Must be implemented by a subclass.")

        def num_children(self, p):
            """Return the number of children that Position p has."""
            raise NotImplementedError("Must be implemented by a subclass.")

        def children(self, p):
            """Generate an iteration of Positions representing p's children."""
            raise NotImplementedError("Must be implemented by a subclass.")

        def __len__(self):
            """Return the total number of elements in the tree."""
            raise NotImplementedError("Must be implemented by a subclass.")

    # Concrete methods implemented in this class

    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0
